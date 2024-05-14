# import boto3
# dynamodb = boto3.client('dynamodb')


# response = dynamodb.update_item(
#     ExpressionAttributeNames={
#         '#AT': 'playerId',
#         '#Y': 'playerName',
#     },
#     ExpressionAttributeValues={
#         ':t': {
#             'N': '111',
#         },
#         ':y': {
#             'S': 'Mohit Jaiswal',
#         },
#     },
#     Key={
#         'playerId': {
#             'N': '111',
#         },
#         'playerName': {
#             'S': 'Virat Kohli',
#         },
#     },
#     ReturnValues='ALL_NEW',
#     TableName='PlayersTable',
#     UpdateExpression='SET #Y = :y, #AT = :t',
# )

# print(response)


import boto3

db = boto3.client('dynamodb')

response = db.update_item(
    TableName = 'StudentTable',

    # Column name to be updated
    ExpressionAttributeNames={
        '#C': 'studentName',
    },

    # Value to be updated
    ExpressionAttributeValues={
        ':t': {
            'S': 'JAY',
        }
    },

    # Where to update
    Key={
        'RollNo': {
            'S': '105',
        }
    },

    UpdateExpression='SET #C = :t',
    # UpdateExpression='SET playerName = :t',
)

print(response)