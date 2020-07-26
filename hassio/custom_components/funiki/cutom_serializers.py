
from homeassistant.helpers.device_registry import DeviceRegistry
from homeassistant.helpers.entity_registry import EntityRegistry
from homeassistant.helpers.area_registry import AreaRegistry
from homeassistant.core import HomeAssistant

class HassIoSerializers :

    @staticmethod
    def summryViewSerializers( hass: HomeAssistant):
        summary = {}
        device_registry = hass.data['device_registry'];
        entity_registry = hass.data['entity_registry'];
        area_registry = hass.data['area_registry'];
        summary.update( {'area' : HassIoSerializers.areaSerializers(areRegistry=area_registry)})
        summary.update( {'entities' : HassIoSerializers.entitySerializers(entityRegistry= entity_registry)})
        summary.update( {'devices' : HassIoSerializers.deviceSerializers(deviceRegistry=device_registry)})
        return summary

    @staticmethod
    def deviceSerializers( deviceRegistry: DeviceRegistry):
        devices = {}
        for key, deviceEntry in deviceRegistry.devices.items():
            devices.update( {key: { 'id' : deviceEntry.id ,
                                    'area_id' : deviceEntry.area_id,
                                    'model' : deviceEntry.model,
                                    'config_entries' : deviceEntry.config_entries ,
                                    'name' :deviceEntry.name
                                    }
                             })
        return devices
    @staticmethod
    def deviceSerializers( deviceRegistry: DeviceRegistry):
        devices = {}
        for key, deviceEntry in deviceRegistry.devices.items():
            devices.update( {key: { 'id' : deviceEntry.id ,
                                    'area_id' : deviceEntry.area_id,
                                    'model' : deviceEntry.model,
                                    'config_entries' : deviceEntry.config_entries ,
                                    'name' :deviceEntry.name
                                    }
                             })
        return devices

    @staticmethod
    def entitySerializers( entityRegistry: EntityRegistry):
        entites = {}

        for key, item in entityRegistry.entities.items():
             entites.update({key:  {'id': item.entity_id,
                                    'domain': item.domain,
                                    'config_entry_id': item.config_entry_id,
                                    'name': item.name ,
                                    'original_name': item.original_name,
                                    'plateform': item.platform ,
                                    'unique_id' : item.unique_id,
                                    'supported_features' :item.supported_features
                                    }
                             })

        return entites


    @staticmethod
    def areaSerializers(areRegistry: AreaRegistry):
        areas = {}
        for key, item in areRegistry.areas.items():
            areas.update({key: {'id': item.id,
                                  'name': item.name
                                  }
                            })
        return areas
