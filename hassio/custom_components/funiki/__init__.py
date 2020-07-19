

import json
import logging
from .cutom_serializers import HassIoSerializers
from homeassistant.components.http import HomeAssistantView
import homeassistant.core as ha
from homeassistant.helpers.service import async_get_all_descriptions
from .const import  ONBOARDING_DOMAIN ,ONBOARDING_STEP_USER ,ONBOARDING_STEP_CORE_CONFIG ,ONBOARDING_STEP_INTEGRATION

_LOGGER = logging.getLogger(__name__)
from .FunikiAreaView import FunikiAreasView ,FunikiAreaDeleteView
from .FunikiUserView import FunikiUserView ,FunikiDeleteUserView
from .FunikiDeviceView import FunikiDeviceView
from .FunikiEntitiesView import FunikiEntitiesView
from .FunikiSummaryView import FunikiSummaryView
from .FunikiOnBoardingStatus import FunikiOnBoardingStatus

DOMAIN = "funiki"


def setup(hass, config):
    hass.http.register_view(FunikiSummaryView)
    hass.http.register_view(FunikiDeviceView)
    hass.http.register_view(FunikiEntitiesView)
    hass.http.register_view(FunikiAreasView)
    hass.http.register_view(FunikiAreaDeleteView)
    hass.http.register_view(FunikiUserView)
    hass.http.register_view(FunikiDeleteUserView)
    hass.http.register_view(FunikiOnBoardingStatus)

    return True

async def async_services_json(hass):
    descriptions = await async_get_all_descriptions(hass)
    return [{"domain": key, "services": value} for key, value in descriptions.items()]


@ha.callback
def async_events_json(hass):
    return [
        {"event": key, "listener_count": value}
        for key, value in hass.bus.async_listeners().items()
    ]
