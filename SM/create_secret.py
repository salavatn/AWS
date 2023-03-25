import boto3

client = boto3.client('secretsmanager')

postgresql = '{"HOST": "db.zorvmuaqwcpbfqjpifmo.supabase.co", "PORT": "5432", ' \
             '"USER": "postgres", "PASSWORD": "zorvmuaqwcpbfqjpifmo", "DB": "postgres"}'
windows = str({'user': 'Administrator', 'password': 'Pa$$wrOrd', 'port': 3389})

# response = client.create_secret(
#     Name='PostgreSQL_1',
#     Description='Variables for connection to Database',
#     KmsKeyId='f68dc523-aecc-4bbd-8247-f729378201e4',
#     SecretString=postgresql)
#
# response2 = client.create_secret(
#     Name='Windows_Server_1',
#     Description='Test variables',
#     SecretString=windows)

response3 = client.create_secret(
    Name='DatabaseProdSecrets',
    SecretString='{"username": "prod", "password": "hello-world-prod"}'
)

'''
response = client.create_secret(
    Name='PostgreSQL',
    ClientRequestToken='string',
    Description='Variables for connection to Database',
    KmsKeyId='f68dc523-aecc-4bbd-8247-f729378201e4',
    SecretBinary=b'bytes',
    SecretString="{'HOST': 'db.zorvmuaqwcpbfqjpifmo.supabase.co', "
                 "'PORT': '5432', 'USER': 'postgres', "
                 "'PASSWORD': 'zorvmuaqwcpbfqjpifmo', 'DB': 'postgres'}",
    Tags=[{'Key': 'string', 'Value': 'string'},],
    AddReplicaRegions=[{'Region': 'string', 'KmsKeyId': 'string'}, ],
    ForceOverwriteReplicaSecret=True | False
)'''