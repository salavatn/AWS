import boto3

client = boto3.client('dynamodb')

table_list = client.list_tables()["TableNames"]

print("\nTable List:")
for table in table_list:
    print(f"\t- {table}")

