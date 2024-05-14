import boto3

iam=boto3.client('iam')

response = iam.list_users(
)
# print(response)
for user in response['Users']:
    print(user['UserName'])