import boto3

bucket_name = 'new-storage3'
filepath = '/home/salavat/Pictures/picture.jpg'
filename = 'photo-7.jpg'

s3_client = boto3.client('s3')
s3_client.upload_file(filepath, bucket_name, filename)
