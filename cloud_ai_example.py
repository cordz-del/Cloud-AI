# Sample code to connect to a cloud AI service
import boto3

# Initialize a client for AWS SageMaker
sagemaker_client = boto3.client('sagemaker')

# Example: List SageMaker models
response = sagemaker_client.list_models()
print(response)
