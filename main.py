import boto3

bucket_name = 'new-storage3'
filepath = '/home/salavat/Pictures/picture.jpg'
filename = 'photo-8.jpg'

s3 = boto3.client('s3')

s3.upload_file(filepath, bucket_name, filename)

