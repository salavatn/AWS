import os


def home(event, context):
    name = os.environ["USER"]
    surname = os.environ["SURNAME"]
    age = os.environ["AGE"]

    data = {
        "message": "Function work correctly!",
        "info": f"{name} {surname}, {age} years old.",
        "input": event
    }

    return data
