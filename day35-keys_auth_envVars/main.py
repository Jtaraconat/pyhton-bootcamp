import requests

API_KEY = "api_key"
API_URL = "api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 51.50731,
    "lon": -0.127758,
    "appid": API_KEY,
    "cnt": 4,
}


response = requests.get(API_URL, params=weather_params)
response.raise_for_status()
data = response.json()
#get id of weather condition
#data["list"][0]["weather"][0]["id"]

#get id weather condition for all returned hours
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        print("bring an umbrella")


#TWILIO FOR SMS 
# from twilio.rest import Client

# account_sid = "account_sid"
# auth_token = "auth_token"
# will_rain = False


# for hour_data in data["list"]:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         body="it's going to rain",
#         from="phone number",
#         to="verified phone number",
#         )
#     print(message.status)