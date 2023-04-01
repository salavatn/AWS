# Key Management Service
import boto3

alias_name = input("Type the alias name: ")
alias = 'alias/' + alias_name

description = input("Type description for Master Key: ")


kms_client = boto3.client("kms")
response = kms_client.create_key(Description=description)

key_id = response["KeyMetadata"]["KeyId"]
arn = response["KeyMetadata"]["Arn"]
kms_client.create_alias(AliasName=alias, TargetKeyId=key_id)

print(f"Created alias {alias} for key {key_id}.")
print(f"ARN: {arn}")


# Note:
# 1. When creating the key, you can add:
#   1.1. Alias Name
#   1.2. Description
#   1.3. User account for API connection
# 2. You can check the keys in WebUI: AWS > Key Management Service (KMS)
