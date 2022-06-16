import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = YOUR_API_KEY
MY_LAT = YOUR_LATITUDE
MY_LONG = YOUR_LONGITUDE
ACCOUNT_SID = YOUR_ACCOUNT_SID
AUTH_TOKEN = YOUR_AUTH_TOKEN
FROM_NUMBER = FROM_CELLPHONE_NUMBER
TO_NUMBER = TO_CELLPHONE_NUMBER

parameters = {
    "appid": API_KEY,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

    client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella! ☂️",
            from_=FROM_NUMBER,
            to=TO_NUMBER,
        )
    print(message.status)
