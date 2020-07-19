
from .cutom_serializers import HassIoSerializers
from homeassistant.components.http import HomeAssistantView
import homeassistant.core as ha

class FunikiSummaryView(HomeAssistantView):
    url = "/api/summary"
    name = "api:summary"
    @ha.callback
    def get(self, request):
        hass = request.app["hass"]
        return self.json_message(HassIoSerializers.summryViewSerializers(hass=hass))

