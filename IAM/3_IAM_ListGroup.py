import boto3

iam=boto3.client('iam')

response = iam.list_groups(
)
# print(response)
for group in response['Groups']:
    print(group['GroupName'])