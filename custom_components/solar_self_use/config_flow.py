"""Config flow for Solar Self Use."""
from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_ENTITY_ID
from homeassistant.helpers import selector
from .const import DOMAIN

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Configure an instance from existing Home Assistant sensors."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            await self.async_set_unique_id("-".join(str(user_input[key]) for key in ['pv_power_entity', 'export_power_entity']))
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title="Solar Self Use", data=user_input)
        schema = vol.Schema({
            vol.Required("pv_power_entity"): selector.EntitySelector(selector.EntitySelectorConfig(domain=["sensor"])),
            vol.Required("export_power_entity"): selector.EntitySelector(selector.EntitySelectorConfig(domain=["sensor"])),
            vol.Required("export_sign", default="positive"): selector.SelectSelector(selector.SelectSelectorConfig(options=['positive', 'negative'], mode=selector.SelectSelectorMode.DROPDOWN)),
        })
        return self.async_show_form(step_id="user", data_schema=schema)

