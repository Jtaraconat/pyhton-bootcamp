import smtplib
import datetime as dt
import random

MY_EMAIL = "my_account@gmail.com"
MY_PASSWORD = "123456789"
OTHER_EMAIL = "other_account_email@gmail.com"


now = dt.datetime.now()
weekday  = now.weekday()

if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=OTHER_EMAIL, msg=f"Subject:Ton message de motivation du lundi\n\n {quote}")