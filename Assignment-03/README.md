Auto-Tagging EC2 Instances on Launch
This project demonstrates how to automatically tag EC2 instances when they are launched using AWS Lambda and EventBridge (CloudWatch Events).

Features
Automatically tags new EC2 instances with:

LaunchDate = current UTC date
Environment = "AutoTagged"
Uses Boto3 to interact with EC2

Event-driven using EventBridge rule for EC2 Instance State-change Notification

Setup Instructions
1. IAM Role for Lambda
Create a new IAM role (lambda-role) with:

Managed Policies:

AmazonEC2FullAccess

AWSLambdaBasicExecutionRole
<img width="933" height="387" alt="image" src="https://github.com/user-attachments/assets/93733315-b080-42dd-bc97-631951a5782c" />
2. Lambda Function
Go to Lambda → Create function

Choose Python 3.x runtime

Assign lambda-role as execution role

Copy lambda_function.py code into the Lambda editor

Set environment variable AWS_REGION if needed (default is current region)

Save and deploy
3. EventBridge Rule
Go to EventBridge → Rules → Create rule

Name: saurabh-trigger-lambda

Rule type: Event pattern

Event pattern:
<img width="874" height="365" alt="image" src="https://github.com/user-attachments/assets/2c6c50bf-ad08-4d0e-8a90-02f7d8c72a0d" />
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running"]
  }
}
Set target as the Lambda function you created
4. (Optional) Debugging & Manual Testing
If tags don’t appear:

Check CloudWatch Logs for the Lambda
Verify Lambda permissions (it needs EC2 tagging rights)
Ensure EventBridge rule is enabled and correctly linked
You can also manually trigger the Lambda with a sample test event:

{
  "detail": {
    "instances": [
      {"instance-id": "i-0abcd1234efgh5678"}
    ]
  }
}
<img width="784" height="341" alt="image" src="https://github.com/user-attachments/assets/38cd1db2-a276-489a-b6b2-38ace384a587" />

