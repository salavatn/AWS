import boto3

kms_client = boto3.client("kms")
response = kms_client.list_keys()


count = 1
for cmk in response["Keys"]:
    key_info = kms_client.describe_key(KeyId=cmk["KeyArn"])
    key_description = key_info["KeyMetadata"]["Description"]

    key_id = cmk["KeyId"]
    key_arn = cmk["KeyArn"]
    print(f"\nKey-{count}:\n"
          f"\tKey ID: \t{key_id} \n"
          f"\tKey ARN: \t{key_arn} \n"
          f"\tDescription: {key_description}")
    count += 1
