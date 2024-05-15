
import boto3

vpc = boto3.client('ec2')

response1 = vpc.create_subnet(
    CidrBlock='192.172.1.0/24',
    VpcId='vpc-058bb5e4a9f4e125a',
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'private-subnet'
                },
            ]
        },
    ]
)

response2 = vpc.create_subnet(
    CidrBlock='192.172.172.0/24',
    VpcId='vpc-058bb5e4a9f4e125a',
    TagSpecifications=[
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'public-subnet'
                },
            ]
        },
    ]
)

print(response1)
print(response2)
