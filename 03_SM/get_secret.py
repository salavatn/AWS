import boto3

service_name = 'secretsmanager'


secret_name = "PostgreSQL_3"
region_name = "eu-central-1"

session = boto3.session.Session()
client = session.client(
    service_name=service_name,
    region_name=region_name)

values = client.get_secret_value(
    SecretId=secret_name)

secret = values['SecretString']
print(secret)