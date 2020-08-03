
from .cutom_serializers import HassIoSerializers
from homeassistant.components.http import HomeAssistantView
import homeassistant.core as ha

class FunikiDeviceView(HomeAssistantView):
    url = "/api/funikidevice"
    name = "api:funiki-device-list"

    @ha.callback
    def get(self, request):
        hass = request.app["hass"]
        device_registry = hass.data['device_registry'];
        return self.json_message(HassIoSerializers.deviceSerializers(deviceRegistry=device_registry))

