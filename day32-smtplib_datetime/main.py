import smtplib 
import datetime as dt

# my_email = "senderaccount@gmail.com"
# password = "123456" #this password must be the one from google account by creating a new app
# other_email = "receiveraccount@mail.com"

# #for hotmail smtp.live.com,  using with to automatically close the connection once it's send
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

#     #tls transport layer security
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=other_email, msg="Subject:first email \n\n This is the body of the email")

#returns date hour
now = dt.datetime.now()
#get only the year
year = now.year
#get number of day of the week indexed 0
day_of_week = now.weekday()

#time by default is 00:00:00
date_of_birth = dt.datetime(year=1991 , month=3 , day=22, hour=12)
print(date_of_birth)