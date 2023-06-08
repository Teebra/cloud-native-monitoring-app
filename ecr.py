import boto3

# Specify your AWS region
region = 'us-east-1'

# Create a session with the specified region
session = boto3.Session(region_name=region)

# Create the ECR client using the session
ecr_client = session.client('ecr')

repository_name = "my-cloud-native-monitoring-repo"

response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)