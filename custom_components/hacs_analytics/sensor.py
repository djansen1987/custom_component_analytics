"""
Get the total install's of installed custom component. More info on: https://www.home-assistant.io/integrations/analytics/
"""

from homeassistant.helpers.aiohttp_client import async_get_clientsession
from datetime import timedelta

import logging

import aiohttp

from homeassistant.components.sensor import (
    SensorEntity,
)
from homeassistant.const import (
    CONF_RESOURCES,
)

from homeassistant.util import Throttle

BASE_URL = 'https://analytics.home-assistant.io/custom_integrations.json'
_LOGGER = logging.getLogger(__name__)

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=60)

SENSOR_PREFIX = 'hacs_'

SENSOR_TYPE_LIST = {
    "total",
    "versions",
}

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):

    """Setup the HACS Analytics."""

    session = async_get_clientsession(hass)
    data = haCustomComponentData(session)
    await data.async_update()

    entities = []
    for sensor_type in SENSOR_TYPE_LIST:
        for components in config[CONF_RESOURCES]:
            if components is not None:
                _LOGGER.warning(sensor_type)
                sensor = haCustomComponentSensors(components,sensor_type, data)
                entities.append(sensor)
    async_add_entities(entities, True)
    return True

class haCustomComponentData(object):

    def __init__(self, session):
        """Initialize the data object."""

        self._session = session
        self._url = BASE_URL
        self._data = None

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def async_update(self):
        """Download and update data from Home Assistant Custom Components API."""

        try:

            response = await self._session.get(self._url)

            if response.status != 200:
                _LOGGER.error(f"{response.url} returned {response.status}")
                return

            ha_custom_components = await response.json()
           
            self._data = ha_custom_components
            _LOGGER.debug(self._data)
            
        # Error logging
        except aiohttp.ClientError:
            _LOGGER.error("Cannot poll eSolar using url: %s")
            return
        except Exception as err:
            _LOGGER.error("Unknown error occurred while polling eSolar: %s", err)
            self._data = None
            return


    @property
    def latest_data(self):
        """Return the latest data object."""
        if self._data:
            return self._data

        _LOGGER.error("return data NONE")
        return None

class haCustomComponentSensors(SensorEntity):
    """Collecting data and return sensor entity."""

    def __init__(self, resource, sensor_type, data):
        """Initialize the sensor."""
        self.entity_name = resource
        self.sensor_type = sensor_type
        self._data = data

        self._state = None
        self._type = self.entity_name
        self._attr_icon = "mdi:github"
        self._attr_state_class = ""
        self._attr_native_unit_of_measurement = "Current Installs"
        self._attr_name = SENSOR_PREFIX + sensor_type + "_" + self.entity_name
        self._attr_device_class = ""
        self._attr_unique_id = f"{SENSOR_PREFIX}_{self.sensor_type}_{self._type}"

        self._discovery = False
        self._dev_id = {}

    @property
    def state(self):
        """Return the state of the sensor. """
        return self._state

    async def async_update(self):
        """Get the latest data and use it to update our sensor state."""
        await self._data.async_update()
        customComponents = self._data.latest_data

        if self.sensor_type is not None:
            if customComponents:
                if self.sensor_type == "total":
                    self._state = int(customComponents[self.entity_name]["total"])
                
                if self.sensor_type == "versions":
                    
                    state_sum = []
                    for version in customComponents[self.entity_name]["versions"]:
                        state_sum.append(str(version) + ": " + str(customComponents[self.entity_name]["versions"][version]))
                    self._state = str(state_sum)
                
                # -Debug- adding sensor
                _LOGGER.warning("Device: {} State: {}".format(self._type, self._state))
