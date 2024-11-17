import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    "108622":
        {
            "last_attendance_time": "2024-11-07 17:24:22",
            "major": "AI ML",
            "name": "Muthu",
            "starting_year": 2016,
            "year": 2,

        },
    "108722":
        {
            "last_attendance_time": "2024-11-07 17:24:15",
            "major": "AI",
            "name": "Vignesh",
            "starting_year": 2015,
            "year": 3
        },
    "108822":
        {
            "last_attendance_time": "2024-11-07 17:24:08",
            "major": "AI Robotics",
            "name": "Raina",
            "starting_year": 2017,
            "year": 1

        }
}

for key, value in data.items():
    ref.child(key).set(value)