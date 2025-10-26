🌐 AWS Lambda EC2 Automation Using Boto3

This project enables automatic management of EC2 instance power states based on predefined tags, using AWS Lambda and Boto3. It helps reduce cloud costs by ensuring instances only run when required.

🎯 Goal of the Automation

Control EC2 instances without manual intervention. Based on the Action tag:

Auto-Start → Instance will be started automatically

Auto-Stop → Instance will be stopped automatically

This keeps your environment clean, optimized, and cost-efficient.

🧩 Implementation Steps
✅ Step 1: EC2 Instance Setup

Created two t2.micro EC2 instances.
Tagged them:
Action: Auto-Stop
Action: Auto-Start
<img width="1339" height="581" alt="image" src="https://github.com/user-attachments/assets/d4316fe0-c129-43a7-b7d8-b4a6eecb2b45" />
2. IAM Role
Created IAM Role: lambda-ec2-manager-role

Attached AmazonEC2FullAccess policy.
<img width="909" height="322" alt="image" src="https://github.com/user-attachments/assets/a657ba66-9208-48a3-b2c4-7c56a9920d8c" />
3. Lambda Function
Runtime: Python 3.x
Permissions: Assigned the above IAM role.
Added Boto3 script to:
Describe instances.
Start/Stop instances based on tags.
4. Testing
Manually triggered Lambda.

Verified EC2 instance states updated correctly.
<img width="717" height="368" alt="image" src="https://github.com/user-attachments/assets/17c32314-cfd7-4392-b203-b2472f212a65" />

Technologies Used
AWS Lambda
Boto3
IAM Roles
EC2


