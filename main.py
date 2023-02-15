import requests
from datetime import datetime

APP_ID = "71c963ed"
API_KEY = "a4fd425987d1fea0c9a3d67a4cfcd79a"

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_config = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 178,
    "age": 33
}

response = requests.post(url=exercise_url, json=exercise_config, headers=exercise_header)
data = response.json()
exercise_data = data["exercises"]
# print(exercise_data)

today = datetime.now()
today_date = today.strftime("%Y/%m/%d")
today_time = today.strftime("%H:%M:%S")

post_url = "https://api.sheety.co/6798f351590850daf9dab91a87ddf63e/workoutTracker/sheet1"

header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer a90e4398gg3024f33g38923"
}

for x in exercise_data:
    post_config = {
        "sheet1": {
            "date": today_date,
            "time": today_time,
            "exercise": x["user_input"].title(),
            "duration": x["duration_min"],
            "calories": x["nf_calories"]
        }
    }

    # response = requests.post(url=post_url, json=post_config, headers=header)
    # print(response.text)

put_url = "https://api.sheety.co/6798f351590850daf9dab91a87ddf63e/workoutTracker/sheet1/2"

put_config = {
        "sheet1": {
            "date": today_date,
            "time": today_time,
            "exercise": "Running",
            "duration": 22,
            "calories": 130
        }
    }

# response = requests.put(url=put_url, json=put_config, headers=header)
# print(response.text)

delete_url = "https://api.sheety.co/6798f351590850daf9dab91a87ddf63e/workoutTracker/sheet1/4"
# response = requests.delete(url=delete_url, headers=header)
# print(response.status_code)
