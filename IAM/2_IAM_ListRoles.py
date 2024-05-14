import boto3

iam=boto3.client('iam')

response = iam.list_roles(
)
# print(response)
for role in response['Roles']:
    print(role['RoleName'])