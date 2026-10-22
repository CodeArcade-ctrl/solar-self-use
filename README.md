# Solar Self Use

**Calculate solar self-consumption and export from PV and grid-export power sensors locally.**

A PV power sensor and a grid-export sensor can show how much solar power is used at home versus sent to the grid. This integration standardizes the direction and reports both watts and a self-use percentage.

## Features

- Solar power used on site in W (PV production minus export, clamped at zero).
- Solar self-use percentage (on-site use divided by PV production).
- Grid export power in W, normalized to a positive value.

The calculation is instantaneous and does not replace the Home Assistant Energy dashboard or energy totals.

## Install with HACS

1. In Home Assistant, open **HACS → Integrations**.
2. Add `https://github.com/CodeArcade-ctrl/solar-self-use` as a custom repository of type **Integration**.
3. Install **Solar Self Use** and restart Home Assistant.
4. Open **Settings → Devices & services → Add integration** and select **Solar Self Use**.

The catalog request is pending review. Until it is accepted, users must add this repository as a custom repository.

## Privacy and limitations

All calculations run locally in Home Assistant. The integration reads only the selected entities and makes no external network requests. Inputs must have valid numeric states; derived values are unavailable while source values are unknown or invalid.

## License

MIT. See [LICENSE](LICENSE).
