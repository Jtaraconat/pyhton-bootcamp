import pandas as pd
import datetime as dt
import smtplib
import random

SENDER_EMAIL = "myemail_account@gmail.com"
MY_PASSWORD = "123456789"


now = dt.datetime.now()
today_tuple = (now.month, now.day)

df = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in df.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy birthday\n\n{content}"
                            )