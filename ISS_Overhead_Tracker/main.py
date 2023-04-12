import requests
import tkinter
from datetime import datetime as dt
import smtplib
import time

continue_checking = True
ISS_overhead = None
MYLAT = 39.723077
MYLNG = 2.807230
MY_EMAIL = "konstantin.kotschenreuther1@gmail.com"



while continue_checking:
    #-------------- Getting ISS Location --------------------- #

    iss_data = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_longitude = float(iss_data.json()["iss_position"]["longitude"])
    iss_latitude = float(iss_data.json()["iss_position"]["latitude"])

    iss_position = (iss_longitude, iss_latitude)
    print(iss_position)


    #------------- Checking for Day/Night --------------------- #

    my_location = {"lat": MYLAT,
                  "lng": MYLNG,
                  "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_location)
    response.raise_for_status()
    response = response.json()

    sunrise_time = response["results"]["sunrise"]
    sunset_time = response["results"]["sunset"]

    sunrise_time = sunrise_time.split("T")
    sunset_time = sunset_time.split("T")

    sunrise_time = sunrise_time[1].split(":")[0]
    sunset_time = sunset_time[1].split(":")[0]

    time_now = dt.now()
    current_hour = time_now.hour

    sunrise_time = int(sunrise_time)
    sunset_time = int(sunset_time)

    if sunrise_time < current_hour < sunset_time:
        pass
    else:
        is_night = True


    # ----------- Checking if ISS overhead ---------------- #

    if MYLAT-5 < iss_latitude < MYLAT+5 and MYLNG-5 < iss_longitude < MYLNG+5:
        ISS_Overhead = True

    if is_night and ISS_overhead:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password= "Kotschi.123")
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="k_kotschenreuther@yahoo.de"
                                , msg=f"Subject: Look Up!\n\n The ISS is overhead, look up :)")
    else:
        print("ISS not overhead")

    time.sleep(60)






