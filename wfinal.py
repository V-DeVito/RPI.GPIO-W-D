import RPi.GPIO as GPIO
import pywapi
import string 
import time

channels = [4, 7, 8, 9, 10, 14, 15, 17, 18, 22, 23, 24, 25]

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(channels, GPIO.OUT)
GPIO.output(channels, 0)


def code():
    weather = pywapi.get_weather_from_weather_com('ZIP Code')
    temperature = int(weather['current_conditions']['temperature'])
    temp_f = temperature * 9 / 5 + 32
    humidity = int(weather['current_conditions']['humidity'])

if humidity >= 80:
    GPIO.output(7, 1)

if humidity <= 79 and humidity >= 60:
    GPIO.output(18, 1)

if humidity <= 59:
    GPIO.output(25, 1)

if temperature >= 90:
    GPIO.output(14, 1)

if temperature <= 89 and temperature >= 80:
    GPIO.output(14, 1)

if temperature <= 79 and temperature >= 70:
    GPIO.output(18, 1)

if temperature <= 69 and temperature >= 40:
    GPIO.output(23, 1)

if temperature <= 39:
    GPIO.output(24, 1)

if cc == 'drizzle' or 'light drizzle' or 'heavy drizzle':
    GPIO.output(4, 1)

if cc == 'rain' or 'light rain':
    GPIO.output(4, 1)

if cc == 'heavy rain':
    GPIO.output(17, 1)

if cc == 'light rain mist' or 'rain mist' or 'heavy rain mist':
    GPIO.output(4, 1)

if cc == 'rain shower' or 'light rain showers':
    GPIO.output(4, 1)

if cc == 'heavy rain shower':
    GPIO.output(17, 1)

if cc == 'light thunderstorm' or 'heavy thunderstorm' or 'thunderstorm':
    GPIO.output(17, 10, 9, HIGH)

if cc == 'light freezing drizzle' or 'heavy freezing drizzle' or 'freezing drizzle':
    GPIO.output(4, 1)

if cc == 'light freezing rain' or 'heavy freezing rain' or 'freezing rain':
    GPIO.output(17, 1)

if cc == 'patches of fog' or 'shallow fog' or 'partial fog' or 'light fog':
    GPIO.output(22, 1)

if cc == 'fog' or 'heavy fog' or 'heavy fog patches' or 'light fog patches':
    GPIO.output(10, 1)

if cc == 'overcast':
    GPIO.output(10, 1)

if cc == 'partly cloudy' or 'scattered clouds':
    GPIO.output(22, 1)

if cc == 'mostly cloudy':
    GPIO.output(10, 1)

while True:
    code()
    time.sleep(180)
    GPIO.cleanup()

