import requests
import os
from twilio.rest import Client
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
parameters={
    "lat":13.435979,
    "lon":79.952507,
    "appid":api_key,
    "cnt":4
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data=response.json()
print(data)
ids = [forecast["weather"][0]["id"] for forecast in data["list"][:4]]
print(ids)
will_rain=False
for i in ids:
    if i <700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="+16614854072",
        body="It's going to rain today. Remember to bring an umbrella☔",
        to="+917780462942"
    )

    print(message.status)
else:print("No rain is expected today. You can step out without an umbrella!")



