## CCA - (Home Assistant) Custom Component Analytics
This component will create an sensor of the current known installations of the configured component's via Home Assistant's Analytics. 
More info on how the Analytics are gathered please visit: https://www.home-assistant.io/integrations/analytics/

## Installation

<!-- ### HACS - Recommended
- Have [HACS](https://hacs.xyz) installed, this will allow you to easily manage and track updates.
- Search for 'custom component analytics'.
- Click Install below the found integration.
- Configure using the configuration instructions below.
- Restart Home-Assistant. -->

### Manual
- Copy directory `custom_components/custom_component_analytics` to your `<config dir>/custom_components` directory.
- Configure with config below.
- Restart Home-Assistant.

## Usage
To use this component in your installation, add the following to your `configuration.yaml` file:

```yaml
sensor:
    - platform: custom_component_analytics
      resources:
          - saj_esolar
          - custom_component_analytics
```
## Screenshot

![alt text](https://github.com/djansen1987/custom_component_analytics/blob/main/screenshots/Home-Assistant-Sensors-CCA-1.png?raw=true "Sensors Example")


## Debugging

Add the relevant lines below to the `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.custom_component_analytics: debug
```

## Donation

Buy me a coffee: <br />
[![Buymeacoffee](https://www.buymeacoffee.com/assets/img/bmc-meta-new/new/apple-icon-120x120.png)](https://www.buymeacoffee.com/djansen1987)

PayPal:<br />
[![Donate](https://github.com/djansen1987/SAJeSolar/blob/main/screenshots/Paypal-Donate-QR-code.png?raw=true)](https://www.paypal.me/djansen1987)<br />
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/djansen1987)
