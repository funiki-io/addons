
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
            devices.update( {key: { 'config_entries' : deviceEntry.config_entries ,
                                    'connections' : deviceEntry.connections,
                                    'identifiers' : deviceEntry.identifiers,
                                    'manufacturer' : deviceEntry.manufacturer ,
                                    'model' :deviceEntry.model,
                                    'name': deviceEntry.name,
                                    'sw_version': deviceEntry.sw_version,
                                    'via_device_id': deviceEntry.via_device_id,
                                    'area_id':deviceEntry.area_id,
                                    'name_by_user': deviceEntry.name_by_user,
                                    'entry_type': deviceEntry.entry_type,
                                    'id' : deviceEntry.id,
                                    'is_new': deviceEntry.is_new
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
                                    'name' :deviceEntry.name,
                                    'connections' : deviceEntry.name,
                                    }
                             })
        return devices

    @staticmethod
    def entitySerializers( entityRegistry: EntityRegistry):
        entites = {}

        for key, item in entityRegistry.entities.items():
             entites.update({key: { 'entity_id': item.entity_id,
                                    'unique_id': item.unique_id,
                                    'platform': item.platform,
                                    'name': item.name ,
                                    'icon': item.icon,
                                    'device_id': item.device_id,
                                    'config_entry_id' : item.config_entry_id,
                                    'disabled_by' :item.disabled_by,
                                    'capabilities': item.capabilities,
                                    'supported_features': item.supported_features,
                                    'unit_of_measurement': item.unit_of_measurement,
                                    'original_name': item.original_name,
                                    'original_icon': item.original_icon,
                                    'domain': item.domain,
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
