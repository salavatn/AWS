from fastapi import FastAPI
from faker import Faker
import json
import requests

fake = Faker()
name = fake.name()


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }


app = FastAPI()


@app.get("/")
async def root():
    return {"data": {"FastAPI": "Hello World"}}


@app.get("/users")
async def get_users():
    msg = f"Hello, {name}!"
    return {"data": {"FastAPI": msg}}


# data = get_users()
# print(f"\n\n{data}")
