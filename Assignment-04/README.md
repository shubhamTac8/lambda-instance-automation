Monitor and Alert on High AWS Billing Using AWS Lambda, Boto3, and SNS

This project shows how to automatically monitor your AWS billing and send alerts via SNS whenever your AWS spending exceeds a set threshold.

🧩 Features

Retrieves the current AWS billing amount using CloudWatch.

Compares the billing total against a predefined threshold (e.g., $50).

Sends email notifications using Amazon SNS when the threshold is exceeded.

Can be scheduled to run daily via EventBridge (formerly CloudWatch Events).

⚙️ Prerequisites

AWS Account with:

CloudWatch Billing Metrics enabled

SNS access

Lambda execution permissions

IAM Role for Lambda must include:

CloudWatchReadOnlyAccess

AmazonSNSFullAccess

🪩 Step 1: Setup SNS

Go to Amazon SNS → Topics → Create topic

Type: Standard

Name: BillingAlertTopic

Create a subscription:

Protocol: Email

Endpoint: your email address

Confirm the subscription by clicking the link in the confirmation email you receive
<img width="947" height="206" alt="image" src="https://github.com/user-attachments/assets/aaa1afb6-d755-4316-bb56-ade79a6d4b8a" />
Step 2: Create IAM Role for Lambda
Go to IAM → Roles → Create role

Choose Trusted entity type: AWS service → Lambda

Attach the following policies:

CloudWatchReadOnlyAccess
AmazonSNSFullAccess
Name the role: LambdaBillingAlertRole

🧠 Step 3: Create Lambda Function
Go to AWS Lambda → Create Function

Choose Author from scratch

Name: BillingMonitorFunction
Runtime: Python 3.12 (or 3.x)
Role: LambdaBillingAlertRole
Paste your billing monitoring code and deploy it.
Step 4: Testing
Option 1: Manual Test
Open your Lambda function.
Click Test → Configure test event → Create new test event.
Name it ManualBillingTest.
Use this sample JSON:
{
  "detail": {
    "action": "manual_test"
  }
}
