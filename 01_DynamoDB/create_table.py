import boto3

dynamodb = boto3.resource('dynamodb')

table_name = "KinderGarten"

attributes = [
    {'AttributeName': 'ID', 'AttributeType': 'N'},
    {'AttributeName': 'Group', 'AttributeType': 'S'}
]
#     {'AttributeName': 'Kid_Name', 'AttributeType': 'S'},
#     {'AttributeName': 'Kid_Surname', 'AttributeType': 'S'},
#     {'AttributeName': 'Kid_Birthday', 'AttributeType': 'S'},
#     {'AttributeName': 'Kid_Age', 'AttributeType': 'N'}

schema = [
    {'AttributeName': 'ID', 'KeyType': 'HASH'},
    {'AttributeName': 'Group', 'KeyType': 'RANGE'}
]

table = dynamodb.create_table(
    AttributeDefinitions=attributes,
    TableName=table_name,
    KeySchema=schema,
    ProvisionedThroughput={'ReadCapacityUnits': 5,'WriteCapacityUnits': 5},
    BillingMode='PROVISIONED'
    )

table.wait_until_exists()
print(table)
