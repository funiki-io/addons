import json
from .cutom_serializers import HassIoSerializers
from homeassistant.components.http import HomeAssistantView
import homeassistant.core as ha

class FunikiOnBoardingStatus(HomeAssistantView):
    url = "/api/onboardingstatus"
    name = "api:onboardingstatus"
    requires_auth = False
    @ha.callback
    def get(self, request):
        hass = request.app["hass"]
        import os.path
        dataDir = "%s/%s/onboarding" % (hass.config.config_dir, '.storage')
        if os.path.exists(dataDir) and os.path.isfile(dataDir) :
            with open(dataDir) as f:
                data = json.load(f)
                hass.data['onboardingstatus'] =data;
                return self.json_message(data)

        return self.json_message({})

