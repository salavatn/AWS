import boto3

s3 = boto3.resource('s3')

print('Existing buckets:')
for bucket in s3.buckets.all():
    print(f"\t{bucket.name}")