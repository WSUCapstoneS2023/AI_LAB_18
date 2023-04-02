import pyrebase
from my_firebase_config import credentials

firebase_instance = pyrebase.initialize_app(credentials)
firebase_database = firebase_instance.database()

# Initializes 'data/incrementing_value' to 0
def initialize_value():
    data = {"incrementing_value": 0}
    firebase_database.child("data").set(data)

# Increments the value in the database at 'data/incrementing_value'
def increment_value():
    record = firebase_database.child("data").get()
    i_value = record.val()['incrementing_value']
    updated_data = {'incrementing_value': i_value + 1}
    firebase_database.child("data").update(updated_data)

if __name__ == "__main__":
    initialize_value()
    increment_value()

