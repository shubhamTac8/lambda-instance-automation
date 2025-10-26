import boto3
import datetime
import os

def lambda_handler(event, context):
    """
    Lambda function to automatically tag new EC2 instances
    when they enter the 'running' state.
    """

    # Initialize EC2 client
    ec2 = boto3.client('ec2', region_name=os.environ.get("AWS_REGION"))

    # Extract instance ID from EventBridge event
    detail = event.get('detail', {})
    instance_id = detail.get('instance-id')

    if not instance_id:
        print("No instance ID found in event.")
        return

    # Create tags
    tags = [
        {
            'Key': 'LaunchDate',
            'Value': datetime.datetime.utcnow().strftime('%Y-%m-%d')
        },
        {
            'Key': 'Environment',
            'Value': 'AutoTagged'
        }
    ]

    try:
        ec2.create_tags(Resources=[instance_id], Tags=tags)
        print(f"Successfully tagged instance: {instance_id} with {tags}")
    except Exception as e:
        print(f"Error tagging instance {instance_id}: {str(e)}")