import boto3

client = boto3.client('secretsmanager')
secrets_dict = client.list_secrets()
secrets_list = secrets_dict["SecretList"]

count = 1
for secret in secrets_list:
    secret_name = secret["Name"]
    values = client.get_secret_value(SecretId=secret_name)
    variables = values['SecretString']

    print(f"Record No{count}:")
    print(f"\t{secret_name}")
    print(f'\t{variables}\n')

    count += 1


'''
# secret:
{'ARN': 'arn:aws:secretsmanager:eu-central-1:864199764664:secret:Windows_Server_3-H6svlE', 
 'Name': 'Windows_Server_3', 
 'Description': 'Test variables', 
 'LastChangedDate': datetime.datetime(2023, 3, 26, 10, 20, 11, 266000, tzinfo=tzlocal()), 
 'LastAccessedDate': datetime.datetime(2023, 3, 26, 3, 0, tzinfo=tzlocal()), 
 'SecretVersionsToStages': {
     '229707a9-a78d-42ac-b3f0-c581e63dfe42': ['AWSCURRENT']}, 
 'CreatedDate': datetime.datetime(2023, 3, 26, 10, 20, 11, 234000, tzinfo=tzlocal())}
'''
'''
# values:
{'ARN': 'arn:aws:secretsmanager:eu-central-1:864199764664:secret:PostgreSQL_3-r85Nqa', 
 'Name': 'PostgreSQL_3', 
 'VersionId': '713137a3-9742-4a58-9669-803453e4b771', 
 'SecretString': '{"HOST": "db.zorvmuaqwcpbfqjpifmo.supabase.co", "PORT": 5432, "USER": "postgres", "PASSWORD": "zorvmuaqwcpbfqjpifmo", "DB": "postgres"}', 
 'VersionStages': ['AWSCURRENT'], 
 'CreatedDate': datetime.datetime(2023, 3, 26, 10, 20, 11, 127000, tzinfo=tzlocal()), 
 'ResponseMetadata': {
     'RequestId': 'e8380d55-3649-490e-99ee-e073e0a70cdf', 
     'HTTPStatusCode': 200, 
     'HTTPHeaders': {
         'x-amzn-requestid': 'e8380d55-3649-490e-99ee-e073e0a70cdf', 
         'content-type': 'application/x-amz-json-1.1', 
         'content-length': '391', 
         'date': 'Sun, 26 Mar 2023 08:26:54 GMT'}, 
     'RetryAttempts': 0}}
'''
