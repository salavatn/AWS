import boto3

### Available parameters:
## accessanalyzer, account, acm, acm-pca, alexaforbusiness, and more...
s3 = boto3.client('s3')

response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'\t\t{bucket["Name"]}')