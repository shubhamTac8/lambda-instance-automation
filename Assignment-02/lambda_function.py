import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    # Define your S3 bucket
    bucket_name = 'my-lambda-cleanup-bucket'  # <-- replace with your actual bucket name

    # Initialize S3 client
    s3 = boto3.client('s3')

    # For testing, delete files older than 1 day (change back to 30 before submission)
    threshold_date = datetime.now(timezone.utc) - timedelta(days=30)

    # List objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' not in response:
        print("Bucket is empty or no files found.")
        return {"status": "No files found"}

    deleted_files = []

    for obj in response['Contents']:
        key = obj['Key']
        last_modified = obj['LastModified']

        # Delete if older than threshold
        if last_modified < threshold_date:
            print(f"Deleting old file: {key} (Last modified: {last_modified})")
            s3.delete_object(Bucket=bucket_name, Key=key)
            deleted_files.append(key)

    if deleted_files:
        print(f"Deleted files: {deleted_files}")
    else:
        print("No files older than threshold were found.")

    return {
        "status": "Cleanup complete",
        "deleted_files": deleted_files
    }