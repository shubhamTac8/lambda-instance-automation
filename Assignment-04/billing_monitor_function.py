import boto3
import datetime
import os

# SNS topic ARN (replace with your own)
SNS_TOPIC_ARN = "arn:aws:sns:eu-west-2:975050024946:saur-BillingAlertTopic"

# Threshold in USD
BILLING_THRESHOLD = 50.0

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
    sns = boto3.client('sns')

    # Get current month and date range
    end_time = datetime.datetime.utcnow()
    start_time = datetime.datetime(end_time.year, end_time.month, 1)

    # Retrieve AWS billing metric
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[
            {'Name': 'Currency', 'Value': 'USD'}
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,  # Daily data points
        Statistics=['Maximum']
    )

    if not response['Datapoints']:
        print("No billing data available yet.")
        return

    latest_datapoint = sorted(response['Datapoints'], key=lambda x: x['Timestamp'])[-1]
    amount = latest_datapoint['Maximum']
    print(f"Current estimated charges: ${amount:.2f}")

    # Compare with threshold
    if amount > BILLING_THRESHOLD:
        message = (
            f"⚠️ AWS Billing Alert ⚠️\n\n"
            f"Your current estimated charges have reached ${amount:.2f}.\n"
            f"Threshold: ${BILLING_THRESHOLD:.2f}\n"
            f"Please check the AWS Billing Dashboard."
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Billing Alert - Threshold Exceeded",
            Message=message
        )
        print("Alert sent to SNS.")
    else:
        print(f"Billing is within limits (${amount:.2f} < ${BILLING_THRESHOLD:.2f}).")