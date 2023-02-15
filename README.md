# AWS

Before using Boto3, you need to set up authentication credentials for your AWS account using either the IAM Console or the AWS CLI. You can either choose an existing user or create a new one.

For instructions about how to create a user using the IAM Console, see Creating IAM users. Once the user has been created, see Managing access keys to learn how to create and retrieve the keys used to authenticate the user.

## Configure AWS CLI
```python
pip install awscli
aws configure
```
```python
AWS Access Key ID [none]:     ****************VQNB 
AWS Secret Access Key [none]: ****************AMAm 
Default region name [none]:   eu-central-1
Default output format [none]: json
```

## Amazon S3 examples
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html

### 1.1 Get list of Buckets via RESOURCE:
```python
import boto3

s3 = boto3.resource('s3')

print('Existing buckets:')
for bucket in s3.buckets.all():
    print(f"\t{bucket.name}")
```
```python
Existing buckets:
	ns-lab-web
	ns-lab.open-storage
```
### 1.2 Get list of Buckets via CLIENT:
```python
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'\t\t{bucket["Name"]}')
```
```python
Existing buckets:
	ns-lab-web
	ns-lab.open-storage
```

### 2. Upload file to Bucket:
```python
import boto3

s3 = boto3.resource('s3')

# Upload a new file
data = open('/home/salavat/Pictures/picture.jpg', 'rb')
s3.Bucket('ns-lab.open-storage').put_object(Key='my_picture.jpg', Body=data)
```