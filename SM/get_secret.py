import json
import boto3

client = boto3.client('secretsmanager')
secrets_dict = client.list_secrets()
secrets_list = secrets_dict["SecretList"]

for secret in secrets_list:
    secret_name = secret["Name"]
    values = client.get_secret_value(SecretId=secret_name)
    variables = json.loads(values['SecretString'])
    print(f"Secret Name:\t{secret_name}")
    print(f'Variables:\t{variables}\n')
