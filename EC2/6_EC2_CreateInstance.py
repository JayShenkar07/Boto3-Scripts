import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

def launch_ec2_instance(image_id, instance_type, key_name, security_group_ids):
    # Launch the EC2 instance
    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_ids],  # SecurityGroupIds should be a list
        MaxCount=1,
        MinCount=1
    )
    
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance {instance_id} is launching...")
    
    return instance_id

def main():
    #Create key pair
    mykey = ec2.create_key_pair(KeyName='boto3key10')
    print("Key pair created")
    key_name = mykey['KeyName']
    print(f"KeyName: {key_name}")

    image_id ='ami-09298640a92b2d12c'
    instance_type = 't2.micro'  
    security_group_ids = 'sg-00a94bf80f9f069d4' 
    
    # Launch the EC2 instance
    instance_id = launch_ec2_instance(image_id, instance_type, key_name, security_group_ids)
    print(f"Instance {instance_id} launched successfully.")

if __name__ == "__main__":
    main()
