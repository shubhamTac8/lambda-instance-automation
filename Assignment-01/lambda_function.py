
import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Stop instances with Action=Auto-Stop
    stop_instances = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    stop_ids = [instance['InstanceId']
                for reservation in stop_instances['Reservations']
                for instance in reservation['Instances']]

    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        print(f"Stopped instances: {stop_ids}")
    else:
        print("No running instances with tag Auto-Stop found.")

    # Start instances with Action=Auto-Start
    start_instances = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    start_ids = [instance['InstanceId']
                 for reservation in start_instances['Reservations']
                 for instance in reservation['Instances']]

    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        print(f"Started instances: {start_ids}")
    else:
        print("No stopped instances with tag Auto-Start found.")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'StoppedInstances': stop_ids,
            'StartedInstances': start_ids
        })
    }
