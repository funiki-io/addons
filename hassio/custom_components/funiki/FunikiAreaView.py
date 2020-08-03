import asyncio
import json
import logging
from .cutom_serializers import HassIoSerializers
from homeassistant.components.http import HomeAssistantView
import homeassistant.core as ha
from homeassistant.helpers.service import async_get_all_descriptions
from .const import  ONBOARDING_DOMAIN ,ONBOARDING_STEP_USER ,ONBOARDING_STEP_CORE_CONFIG ,ONBOARDING_STEP_INTEGRATION
_LOGGER = logging.getLogger(__name__)

from homeassistant.const import HTTP_BAD_REQUEST
class FunikiAreasView(HomeAssistantView):
    url = "/api/funikiarea"
    name = "api:funiki-area"

    @ha.callback
    def get(self, request):
        hass = request.app["hass"]
        entity_registry = hass.data['area_registry'];
        return self.json_message(HassIoSerializers.entitySerializers(entityRegistry=entity_registry))

    @ha.callback
    async def post(self, request):
        hass = request.app["hass"]
        area_registry = hass.data['area_registry'];

        data = None
        try:
            data = await request.json()
        except ValueError:
            if not self._allow_empty or ( request.content.read()) != b"":
                _LOGGER.error("Invalid JSON received")
                return self.json_message("Invalid JSON.", HTTP_BAD_REQUEST)
        try :
            area = area_registry.async_create( data.get('name'))
        except Exception as  e:
            return self.json_message(str(e) , HTTP_BAD_REQUEST)

        return self.json_message(area.id)



class FunikiAreaDeleteView(HomeAssistantView):
    url = "/api/funikiarea/{area_id}"
    name = "api:funiki-area:delete"

    @ha.callback
    async def delete(self, request , area_id):
        hass = request.app["hass"]
        area_registry = hass.data['area_registry'];
        try :
            area = await area_registry.async_delete(area_id)
        except Exception as  e:
            return self.json_message('unable to delete are' , HTTP_BAD_REQUEST)

        return self.json_message(area_id)

    @ha.callback
    async def put(self, request , area_id):
        hass = request.app["hass"]
        area_registry = hass.data['area_registry'];

        data = None
        try:
            data = await request.json()
        except ValueError:
            if not self._allow_empty or (request.content.read()) != b"":
                _LOGGER.error("Invalid JSON received")
                return self.json_message("Invalid JSON.", HTTP_BAD_REQUEST)
        try:
            area = area_registry.async_update(area_id, data.get('name'))
        except Exception as  e:
            return self.json_message(str(e), HTTP_BAD_REQUEST)

        return self.json_message(area.id)