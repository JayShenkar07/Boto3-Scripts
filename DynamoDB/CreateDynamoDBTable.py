import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
      KeySchema=[
        {
            'AttributeName': 'userName',
            'KeyType': 'HASH',  # HASH indicates the partition key.
        },
    ],

    AttributeDefinitions=[
        {
            'AttributeName': 'userName',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'password',
            'AttributeType': 'S',
        },
    
    ],
  
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
    TableName='UserTable',
)

print(response)
