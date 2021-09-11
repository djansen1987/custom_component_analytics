## Hacs Analytics Component
This component will create an sensor of the current known installations of your component by Home Assistant's Analytics. 
More info on how the Analytics are gathered please visit: https://www.home-assistant.io/integrations/analytics/
## Installation

### HACS - Recommended
- Have [HACS](https://hacs.xyz) installed, this will allow you to easily manage and track updates.
- Search for 'HACS Analytics'.
- Click Install below the found integration.
- Configure using the configuration instructions below.
- Restart Home-Assistant.

### Manual
- Copy directory `custom_components/hacs_analytics` to your `<config dir>/custom_components` directory.
- Configure with config below.
- Restart Home-Assistant.

## Usage
To use this component in your installation, add the following to your `configuration.yaml` file:

```yaml
sensor:
    - platform: hacs_analytics
    resources:
        - saj_esolar
        - hacs
        - smartthinq_sensors
```
## Screenshot

![alt text](https://github.com/djansen1987/hacs_analytics/blob/main/screenshots/Home-Assistant-Sensors-hacs_analytics-1.png?raw=true "Sensors Example")


## Debugging

Add the relevant lines below to the `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.hacs_analytics: debug
```
## Credits

Credits to @cyberjunky. I got inspired by his source code which helped me a lot to create my first Custom Component.
https://github.com/cyberjunky/home-assistant-toon_smartmeter/

## Donation

Buy me a coffee: <br />
[![Buymeacoffee](https://www.buymeacoffee.com/assets/img/bmc-meta-new/new/apple-icon-120x120.png)](https://www.buymeacoffee.com/djansen1987)

PayPal:<br />
[![Donate](https://github.com/djansen1987/SAJeSolar/blob/main/screenshots/Paypal-Donate-QR-code.png?raw=true)](https://www.paypal.me/djansen1987)<br />
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/djansen1987)
