import boto3
import os

def backup_to_s3(local_directory, bucket_name, s3_folder):
    s3 = boto3.resource('s3')
    for root, dirs, files in os.walk(local_directory):
        for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = os.path.join(s3_folder, relative_path)
            
            try:
                s3.Bucket(bucket_name).upload_file(local_path, s3_path)
                print(f"Uploaded {local_path} to {s3_path} in bucket {bucket_name}")
            except Exception as e:
                print(f"Failed to upload {local_path} due to {str(e)}")
            finally:
                # Any cleanup code, if needed, can be added here
                pass

# Example usage:
local_directory = "/path/to/your/local/directory"
bucket_name = "my-unique-bucket-name-12345"
s3_folder = "backup_folder"

try:
    backup_to_s3(local_directory, bucket_name, s3_folder)
except Exception as e:
    print(f"An error occurred: {str(e)}")