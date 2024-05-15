
import boto3

s3 = boto3.client('s3')

response = s3.put_object(
    Body='S3/image.png',
    Bucket='bucket-using-boto3-02-05-2024',
    Key='myimg',              
)

print(response)

