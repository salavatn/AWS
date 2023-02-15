# AWS

You will learn "How to":
1. [Done] Create new Bucket
2. [Done] Get list Bucket
    - Get via RESOURCE
    - Get via CLIENT
3. [Done] Upload file to Bucket
- Check uploaded files
- Delete file from Bucket
- Delete Bucket

Before using Boto3, you need to set up authentication credentials for your AWS account using either the IAM Console or the AWS CLI. You can either choose an existing user or create a new one.

For instructions about how to create a user using the IAM Console, see Creating IAM users. Once the user has been created, see Managing access keys to learn how to create and retrieve the keys used to authenticate the user.

## Configure AWS CLI
```sh
pip install awscli
aws configure
```
```output
AWS Access Key ID [none]:     ****************VQNB 
AWS Secret Access Key [none]: ****************AMAm 
Default region name [none]:   eu-central-1
Default output format [none]: json
```

## Amazon S3 examples
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html

## 1. Create new Bucket
```python
import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    """
    Create an S3 bucket in a specified region
    :param bucket_name: Bucket name
    :param region: set region, example: us-west-2
    :return: True if bucket created, else False
    """

    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as error:
        logging.error(error)
        return False
    return True


create_bucket("new-storage3", "eu-central-1")
```

## 2. Get list of Bucket
### 2.1. Get via RESOURCE:
```python
import boto3

s3 = boto3.resource('s3')

print('Existing buckets:')
for bucket in s3.buckets.all():
    print(f"\t{bucket.name}")
```
```output
Existing buckets:
	new-storage3
	ns-lab-web
	ns-lab.open-storage
```


### 2.2. Get via CLIENT:
```python
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'\t\t{bucket["Name"]}')
```
```output
Existing buckets:
	new-storage3
	ns-lab-web
	ns-lab.open-storage
```


## 3. Upload file to Bucket
### Upload via "RESOURCE" and "PUT_OBJECT"
```python
import boto3

bucket_name = 'new-storage3'
filepath = '/home/salavat/Pictures/picture.jpg'
filename = 'photo-6.jpg'

s3 = boto3.resource('s3')

file = open(filepath, 'rb')
bucket = s3.Bucket(bucket_name)
bucket.put_object(Key=filename, Body=file)
```

### Upload via "CLIENT" and "UPLOAD_FILE"
```python
import boto3

bucket_name = 'new-storage3'
filepath = '/home/salavat/Pictures/picture.jpg'
filename = 'photo-7.jpg'

s3 = boto3.client('s3')

s3.upload_file(filepath, bucket_name, filename)
```