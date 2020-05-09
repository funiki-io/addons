"""Rest API for Home Assistant."""
import asyncio
import json
import logging
from .cutom_serializers import HassIoSerializers
from homeassistant.components.http import HomeAssistantView
import homeassistant.core as ha
from homeassistant.helpers.service import async_get_all_descriptions

_LOGGER = logging.getLogger(__name__)

DOMAIN = "funiki"


def setup(hass, config):
    hass.http.register_view(FunikiSummaryView)
    hass.http.register_view(FunikiDeviceView)
    hass.http.register_view(FunikiEntitiesView)
    hass.http.register_view(FunikiAreaView)
    return True


class FunikiSummaryView(HomeAssistantView):
    url = "/api/summary"
    name = "api:summary"

    @ha.callback
    def get(self, request):
        hass = request.app["hass"]
        return self.json_message(HassIoSerializers.summryViewSerializers(hass=hass))


class FunikiDeviceView(HomeAssistantView):
    url = "/api/hassio/device"
    name = "api:hassio-device-list"

    @ha.callback
    def get(self, request):
        hass = request.app["hass"]
        device_registry = hass.data['device_registry'];
        return self.json_message(HassIoSerializers.deviceSerializers(deviceRegistry=device_registry))


class FunikiEntitiesView(HomeAssistantView):
    url = "/api/hassio/entites"
    name = "api:hassio-entites-list"

    @ha.callback
    def get(self, request):
        hass = request.app["hass"]
        entity_registry = hass.data['entity_registry'];
        return self.json_message(HassIoSerializers.entitySerializers(entityRegistry=entity_registry))


class FunikiAreaView(HomeAssistantView):
    url = "/api/hassio/area"
    name = "api:hassio-are-list"

    @ha.callback
    def get(self, request):
        hass = request.app["hass"]
        area_registry = hass.data['area_registry'];
        return self.json_message(HassIoSerializers.areaSerializers(areRegistry=area_registry))

async def async_services_json(hass):
    """Generate services data to JSONify."""
    descriptions = await async_get_all_descriptions(hass)
    return [{"domain": key, "services": value} for key, value in descriptions.items()]


@ha.callback
def async_events_json(hass):
    """Generate event data to JSONify."""
    return [
        {"event": key, "listener_count": value}
        for key, value in hass.bus.async_listeners().items()
    ]
