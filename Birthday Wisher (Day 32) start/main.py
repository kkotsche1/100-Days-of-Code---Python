import smtplib
from random import randint

my_email = "konstantin.kotschenreuther1@gmail.com"




import datetime as dt


with open("quotes.txt", "r") as quote_file:
    quotes = quote_file.readlines()


random_quote_index = randint(1,102)
random_quote = quotes[random_quote_index]
random_quote = random_quote.strip()


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()

if weekday == 3:
    print("hello")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password = "Kotschi.123")
        connection.sendmail(from_addr=my_email, to_addrs="k_kotschenreuther@yahoo.de",
                         msg=f"Subject:This email was sent through Python\n\n Hello Konstantin, your motivational wednesday "
                             f"quote is: {random_quote}")
        connection.close()


date_of_birth = dt.datetime(year = 1997, month = 11, day = 1)