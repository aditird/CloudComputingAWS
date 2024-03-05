import boto3


ec2_client = boto3.resource(
      'ec2',
      region_name='us-east-1', aws_access_key_id='<ID>', aws_secret_access_key='<key>')

ami_id = "ami-00ddb0e5626798373"

instance = ec2_client.create_instances(ImageId=ami_id,MinCount=1,MaxCount=1,InstanceType="t2.micro",KeyName='my_key_pair', TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key': 'Name','Value': 'WebTier' }]}])



# ec2_client1 = boto3.client(
#     'ec2',
#     region_name='us-east-1',
#     aws_access_key_id='AKIA4MTWKYMB6C3CDJJT',
#     aws_secret_access_key='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'
# )

# response = ec2_client1.run_instances(ImageId=ami_id, MinCount=1,MaxCount=1,InstanceType="t2.micro",TagSpecifications=[{'ResourceType': 'instance','Tags': [{'Key': 'Name','Value': 'WebTier Worker' }]}])

# instance = response['Instances'][1]

# print(f"Launched instance with ID: {instance['InstanceId']}")
