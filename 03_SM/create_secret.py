import boto3

client = boto3.client('secretsmanager')


windows = '{"user": "Administrator", "IP Address": "192.168.1.145", "password": "Pa$$wrOrd", "port": 3389}'
aws_sc_name = 'Windows_Server_2012-R2'
aws_sc_description = 'Test variables'
aws_kms_key = 'f68dc523-aecc-4bbd-8247-f729378201e4'


response = client.create_secret(
    Name=aws_sc_name,
    Description=aws_sc_description,
    KmsKeyId=aws_kms_key,
    SecretString=windows)


'''
# EXAMPLE:
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
