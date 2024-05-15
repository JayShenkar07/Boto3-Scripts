
import boto3

s3 = boto3.client('s3')

response = s3.delete_bucket(
    Bucket='bucket-using-boto3-02-05-2024'
)

print(response)