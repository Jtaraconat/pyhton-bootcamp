import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "my_email_account@gmail.com"
MY_PASSWORD = "123456789"
MY_LAT = 51.507351
MY_LNG = -0.127758


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    #raise an error for all code != of success
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LNG - 5) <= iss_longitude <= (MY_LNG + 5):
        return True
    
def is_night():
    #API call with parameters
    parameters = {
    "lat":MY_LAT ,
    "lng": MY_LNG,
    "formatted": 0
    }
    now = datetime.now().hour
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    #get results and split to get the hour 
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if now >= sunset or now <= sunrise:
        return True

#execute the code every 60 seconds
while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: ISS passing by\n\nLook up!")








