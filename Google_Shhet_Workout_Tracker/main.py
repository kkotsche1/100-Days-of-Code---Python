import requests
from datetime import datetime

# ---------- Setting up API Parameters for Exercise retreival ----- #

APP_ID= "9e54025f"
API_KEY= "25353c4356218e4c74919cc613d5824e"
API_ENDPOINT= "https://trackapi.nutritionix.com/v2/natural/exercise"


headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id": "0"
}

natural_lang = {
    "query": input("What exercises did you do today?"),
    "gender":"male",
    "weight_kg":70,
    "height_cm":183,
    "age":24
}

# ------------------ Getting Exercise Information ---------------- #

request = requests.post(url=API_ENDPOINT, headers=headers, json=natural_lang)
raw_data = request.json()
exercises = raw_data["exercises"]

exercise_name=[]
time=[]
calories_burned=[]

for exercise in exercises:
    exercise_name.append(exercise["name"].title())
    time.append(exercise["duration_min"])
    calories_burned.append(exercise["nf_calories"])



# ----------- Writing Exercises to Google Sheets ---------- #

SHEETY_ENDPOINT = "https://api.sheety.co/eca441825d96ccddfdce454f7b898e53/myWorkouts/workouts"

i = 0
request = requests.get("https://api.sheety.co/eca441825d96ccddfdce454f7b898e53/myWorkouts/workouts")
print(request.json())
while i < len(exercise_name):

    now = datetime.now()

    parameters = {
        "workout": {
            "time": now.strftime('%H:%M:%S'),
            "exercise": exercise_name[i],
            "duration": time[i],
            "calories": calories_burned[i],
            "date": now.strftime('%d/%m/%Y')
        }
    }

    request = requests.post(url=SHEETY_ENDPOINT, json=parameters)
    print(request)

    i+=1