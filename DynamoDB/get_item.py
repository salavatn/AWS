import boto3

client = boto3.client('dynamodb')

table_list = client.list_tables()["TableNames"]
for table in table_list:
    # print(f"Table: {table}")
    pass

methods = dir(client)
search = "item"
for element in methods:
    if search in element:
        # pass
        print(element)
