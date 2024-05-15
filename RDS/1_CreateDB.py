import boto3

# Initialize the RDS client
rds = boto3.client('rds')

# Create RDS MySQL instance
response = rds.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.t3.micro',  # t3.micro is a supported instance class
    DBInstanceIdentifier='mymysqlinstance',
    Engine='mysql',  
    EngineVersion='8.0.35',  # Ensure EngineVersion matches a supported version
    LicenseModel='general-public-license',
    MasterUserPassword='botomj123456',
    MasterUsername='boto_user',
)

print(response)
