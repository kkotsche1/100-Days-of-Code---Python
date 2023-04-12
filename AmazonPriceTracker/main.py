import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

AMAZON_LINK = "https://www.amazon.de/Razer-DeathAdder-Maus-Switches-" \
              "Akku-Laufzeit-Verbindungsmodi/dp/B08GCQ5TBJ/ref=sr_1_18"
my_email = "konstantin.kotschenreuther1@gmail.com"
HEADERS = {
    "qid": "1647378489",
    "__mk_de_DE": "%C3%85M%C3%85%C5%BD%C3%95%C3%91",
    "crid": "153ZC8FR2F979",
    "sr": "8-18",
    "th": "1"
}

# request = requests.get(AMAZON_LINK, "lxml.parser", headers=HEADERS)
# print (request.text)
#
# soup = BeautifulSoup(request.text, parser="lxml", features="lxml")
# price = soup.find(name = "span", class_="a-offscreen")
# price= price.text()

price = "90,99€"

price = price.replace("€","")
price = price.split(",")
print(price)
euro_amount = float(price[0])
cent_amount = float(price[1])/100

total_price = euro_amount+cent_amount
print(total_price)

try:
    with open("price_tracker.txt", "r") as file:
        current_low_price = float(file.read())
except:
    current_low_price = 100000000.00

print(current_low_price)

if total_price < current_low_price:
    with open("price_tracker.txt", "w") as file:
        file.truncate(0)
        file.write(f"{total_price}")
        print("success")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="Kotschi.123")
        connection.sendmail(from_addr=my_email, to_addrs="k_kotschenreuther@yahoo.de",
                            msg=f"Subject:New low price for your Razer Mouse!\n\n Hello Konstantin, the new low price for the Razer Mouse is: "
                                f"quote is: {total_price}")
        connection.close()