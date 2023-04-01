import boto3

client = boto3.client('dynamodb')

table_name = "Notes"
partition_key = "Notes_ID"
id = '2'

response = client.get_item(
    TableName=table_name, 
    Key={partition_key: {"N": id} }
    )


print("\nItems:")
for element in response["Item"]:
    key = list(response["Item"][element].keys())[0]
    value = response["Item"][element][key]
    print(element)
    print(f"\t- {value}")


