# RPI.GPIO-W-D

Raspberry Pi LED GPIO Weather Display v1.0.0

* Must download PYWAPI from: https://code.google.com/archive/p/python-weather-api/
* Credit to the authors stated on that page.
* See GPIO and diagram for pinouts.
* Set ZIP Code in this line:
  * weather = pywapi.get_weather_from_weather_com('ZIP code')





Understanding Current Condition LEDS:

* Rain/Drizzle:
* Heavy Rain:
* Thunderstorms:
* Fog:
* Partly Cloudy:
* Mostly Cloudy:
* Clear:

* *In the actual API documentation, there are more than just those 7 conditions. In fact, there are about 55+. It would be painful to have a LED for each of those conditions, so I condensed it down to 7 conditions. This is designed to be simple. I hope you enjoy it.
