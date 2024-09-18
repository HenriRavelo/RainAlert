import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv('.env')


parameters = {
    'lat': -18.9137,
    'lon': 47.5361,
    'cnt': 4,
    'appid': os.getenv("TWILIO_API_KEY"),
}
client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))

r = requests.get(url='https://api.openweathermap.org/data/2.5/forecast?', params=parameters)
r.raise_for_status()
weather = r.json()
good_day = False
for i in range(4):
    if weather['list'][i]['weather'][0]['id'] < 700:
        print('Bring an umbrella')
    else:
        message = client.messages.create(
            body=f"Bonjour {weather['city']['name']}, La météo d'aujourd'hui?\n  Soleil☀️.",
            from_=os.getenv("TWILIO_number"),
            to=os.getenv("RECEIVER_NUMBER"))
        print(message.status)
        break
