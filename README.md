# RPI.GPIO-W-D

Raspberry Pi LED GPIO Weather Display v1.0.0

* Must download PYWAPI from: https://code.google.com/archive/p/python-weather-api/
* Credit to the authors stated on that page.
* See GPIO and diagram for pinouts.
* Set ZIP Code in this line:
  * weather = pywapi.get_weather_from_weather_com('ZIP code')





Understanding Current Condition LEDS:

Check Diagram

* Rain/Drizzle: 9
* Heavy Rain: 10
* Thunderstorms: 10,12,13
* Fog: 12
* Partly Cloudy: 11
* Mostly Cloudy: 12
* Clear: None

Temperature LEDS:

* Hot: 1
* Warm: 2
* Moderate: 3
* Cold: 4
* Freezing: 5

Humidity LEDS:

* Very Humid: 8
* Moderately Humid: 7
* Slightly Humid: 6


* *In the actual API documentation, there are more than just those 7 conditions. In fact, there are about 55+. It would be painful to have a LED for each of those conditions, so I condensed it down to 7 conditions. This is more for getting a general weather description, rather than an exact measurement This is designed to be simple. I hope you enjoy it.
