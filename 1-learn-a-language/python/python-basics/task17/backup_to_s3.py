import boto3
import os

def backup_to_s3(local_directory, bucket_name, s3_folder):
    # Create an S3 resource
    s3 = boto3.resource('s3')

    # Walk through the local directory
    for root, dirs, files in os.walk(local_directory):
        for filename in files:
            # Construct the full local path
            local_path = os.path.join(root, filename)

            # Construct the full S3 path
            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = os.path.join(s3_folder, relative_path)

            # Upload to S3
            s3.Bucket(bucket_name).upload_file(local_path, s3_path)
            print(f"Uploaded {local_path} to {s3_path} in bucket {bucket_name}")

# Example usage:
local_directory = "/path/to/your/local/directory"  # Replace with your local directory path
bucket_name = "my-unique-bucket-name-12345"  # Replace with your S3 bucket name
s3_folder = "backup_folder"  # Replace with your desired folder name in S3

backup_to_s3(local_directory, bucket_name, s3_folder)