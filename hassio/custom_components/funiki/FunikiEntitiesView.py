
from .cutom_serializers import HassIoSerializers
from homeassistant.components.http import HomeAssistantView
import homeassistant.core as ha

class FunikiEntitiesView(HomeAssistantView):
    url = "/api/funikientites"
    name = "api:funiki-entites-list"
    requires_auth = False
    @ha.callback
    def get(self, request):
        hass = request.app["hass"]
        entity_registry = hass.data['entity_registry'];
        return self.json_message(HassIoSerializers.entitySerializers(entityRegistry=entity_registry))

