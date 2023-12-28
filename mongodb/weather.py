# Do not forget to create a variable in your console with the export command
# You can choose the city of your choice, you only need to write the name in english

# You will need to create a variable WEATHER with your key of OpenWeatherMap

import os 
import requests

WEATHER = "5d65d4e07f500717f5c4c14d26d5e47b"
KEY = os.getenv(WEATHER)
CITY = "COURBEVOIE"


r = requests.get(
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
        CITY, KEY
    )
)

print(r.json())