import logging
from homeassistant.components.http import HomeAssistantView
import homeassistant.core as ha
_LOGGER = logging.getLogger(__name__)
from homeassistant.auth.providers import homeassistant as auth_ha

from homeassistant.const import HTTP_BAD_REQUEST
class FunikiUserView(HomeAssistantView):
    url = "/api/funiki/user"
    name = "api:funiki:user"
    requires_auth = False

    @ha.callback
    async def post(self, request):
        hass = request.app["hass"]
        provider =_get_provider(hass)
        await provider.async_initialize()

        msg = None
        try:
            msg = await request.json()
        except ValueError:
            if not self._allow_empty or ( request.content.read()) != b"":
                _LOGGER.error("Invalid JSON received")
                return self.json_message("Invalid JSON.", HTTP_BAD_REQUEST)

        try :
            user = await hass.auth.async_create_user(msg["name"], msg.get("group_ids"))
        except Exception as  e:
            return self.json_message(str(e) , HTTP_BAD_REQUEST)

        try:
            await hass.async_add_executor_job(
                provider.data.add_auth, msg["username"], msg["password"]
            )
        except auth_ha.InvalidUser:
            await hass.auth.async_remove_user(user)
            return self.json_message("Username already exists", HTTP_BAD_REQUEST)

        try :
            credentials = await provider.async_get_or_create_credentials(
                {"username": msg["username"]}
            )
            await hass.auth.async_link_user(user, credentials)
            await provider.data.async_save()
        except Exception as  e:
            if credentials is not None:
                await hass.auth.async_remove_credentials(credentials)
            if user is not None:
                await hass.auth.async_remove_user(user)
            return self.json_message("Error while creating User", HTTP_BAD_REQUEST)

        return self.json_message(user.id)



class FunikiDeleteUserView(HomeAssistantView):
    url = "/api/funiki/user/{user_id}"
    name = "api:funiki:delete:user"
    requires_auth = False

    @ha.callback
    async def delete(self, request, user_id):
        hass = request.app["hass"]
        try :
            user = await hass.auth.async_get_user(user_id)
        except Exception as  e:
            return self.json_message(str(e) , HTTP_BAD_REQUEST)

        if user is None:
            return self.json_message('User not found', HTTP_BAD_REQUEST)

        try :
            await hass.auth.async_remove_user(user)
        except Exception as  e:
            return self.json_message(str(e) , HTTP_BAD_REQUEST)

        return self.json_message(user.id)


def _get_provider(hass):
        for prv in hass.auth.auth_providers:
            if prv.type == "homeassistant":
                return prv

        raise RuntimeError("Provider not found")
