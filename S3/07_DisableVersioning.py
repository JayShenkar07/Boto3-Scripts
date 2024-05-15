
import boto3

s3 = boto3.client('s3')

response = s3.put_bucket_versioning(
    Bucket='bucket-using-boto3-02-05-2024',
    VersioningConfiguration={
        # 'Status': 'Enabled'
        'Status': 'Suspended'
    }
)
print(response)