import boto3;

db = boto3.client('dynamodb')


response = db.get_item(
    Key={
        'RollNo': {
            'S': '105',
        },
    },
    TableName='StudentTable',
)

print(response)




# # Full table
# response = db.scan(
#     TableName = 'StudentTable'
# )

# print("\n")
# print(response)