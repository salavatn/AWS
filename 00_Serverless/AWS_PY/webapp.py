import boto3
import json
import os



def based(event, context):
    # time.sleep(4)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

client = boto3.client('lambda')
def boto3_test(event, context):
    response = client.list_functions()
    return response


def get_variable(event, context):
    name = os.environ['MY_FIRST_NAME']
    syrname = os.environ['MY_SECOND_NAME']
    var_location = os.environ['My_ENV_LOCATION']

    data = f"{name} {syrname}"
    return {"UserData": data, "VarEnvLocation": var_location}



