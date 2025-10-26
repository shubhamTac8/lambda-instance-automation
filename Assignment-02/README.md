🧹 Automated S3 Bucket Cleanup Using AWS Lambda & Boto3

Effortless housekeeping for your S3 storage. This automation clears outdated files so your bucket stays clean and cost-efficient.

🎯 Objective

Build an AWS Lambda function that automatically removes objects older than 30 days from a specified S3 bucket.
No manual cleanup. No unused storage growing endlessly.

🏗️ Project Overview

This setup uses AWS Lambda + Boto3 to:

Scan objects inside an S3 bucket

Check their last modified timestamp

Delete files exceeding the configured age limit (default: 30 days)

Perfect for logs, temporary uploads, or regular backups.

⚙️ Setup Instructions
✅ Step 1: Create an S3 Bucket

Navigate to the AWS S3 console

Create a bucket (example: lambda-auto-clean-bucket)

Upload some sample files to simulate aged data
<img width="878" height="255" alt="image" src="https://github.com/user-attachments/assets/26d19432-b84b-4732-88b3-7e43f18775c8" />
2️⃣ Create an IAM Role
Go to AWS IAM → Roles → Create Role → AWS Service → Lambda.

Attach AmazonS3FullAccess policy.

Name it lambda-s3-cleanup-role.
3️⃣ Create Lambda Function
Runtime: Python 3.x

Attach the IAM role above.

4️⃣ Deploy and Test
Click Deploy in the Lambda console.

Click Test and run a manual invocation.

Check CloudWatch logs or S3 bucket to verify deleted files.
<img width="767" height="432" alt="image" src="https://github.com/user-attachments/assets/054d8de5-ce20-48e3-aaf3-de48e33da66b" />


