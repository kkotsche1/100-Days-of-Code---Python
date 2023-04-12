import requests
import datetime as dt
rain_today = False

# ---------------- Accessing current Time ------------#
def time_checker():

    hour_time = dt.datetime.now()
    hour = hour_time.hour
    minute = hour_time.minute

    if hour == 8 and minute == 0:
        return True
    else:
        return False



#------------ Accessing weather conditions ----------------#
#------------ function returns list of hourly conditions for next 12 hours ------ #


API_KEY = "b3473736a487694b332e8c6816543f22"
LAT = 39.706821
LON = 2.790640

def get_hourly_forecast():



    params = {
        "lat": LAT,
        "lon": LON,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                            params=params)
    print(response.status_code)
    weather_data = response.json()
    hourly_forecasts = weather_data["hourly"]
    hourly_weather = []

    for day in hourly_forecasts[:12]:
        weather = day["weather"]
        condition = weather[0]
        condition = condition["main"]
        hourly_weather.append(condition)
    print(hourly_weather)
    return hourly_weather


#--------------- Checking for Rain in the next 12 hours ------------ #

def rain_checker(hourly_weather):

    if "Rain" in hourly_weather:
        return True
    else:
        return False


# ---------------- Sending SMS if it Rains --------------------- #

def send_message(rain):
    from twilio.rest import Client

    API_KEY_TWILIO = "29ab14e21da397b163590918e0d4da11"
    SID_TWILIO = "AC85b4dccb465482509b8b7dc2d653e166"

    client = Client(SID_TWILIO, API_KEY_TWILIO)

    if rain:
        message = client.messages.create(
            to="+4915123916438",
            from_="+19127158761",
            body="It is going to rain today ☂️"

        )
        print(message.status)

    if not rain:
        message = client.messages.create(
            to="+4915123916438",
            from_="+19127158761",
            body="It is not going to rain today 🌂"

        )
        print(message.status)

#-------- Running Program ---------#


time_to_run = time_checker()

hourly_forecast = get_hourly_forecast()
today_rain = rain_checker(hourly_forecast)

send_message(today_rain)
