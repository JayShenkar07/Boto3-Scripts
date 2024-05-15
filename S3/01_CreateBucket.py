import boto3
s3 = boto3.client('s3')

#Create bucket
bucket_name = 'bucket-using-boto3-02-05-2024'
region = 'ap-south-1'  

location_constraint = {'LocationConstraint': region}

# Create the bucket with region specified
response1 = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location_constraint
)

print(response1)