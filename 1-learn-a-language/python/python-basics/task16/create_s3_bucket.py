import boto3

def create_bucket(bucket_name, region=None):
    # Create an S3 client
    s3 = boto3.client('s3', region_name=region)

    # Create the S3 bucket
    if region is None:
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})

    print(f"Bucket {bucket_name} created successfully!")

# Example usage:
bucket_name = "my-unique-bucket-name-12345"  # Change this to your desired unique bucket name
region = "us-west-1"  # Change this to your desired region or set to None for the default region
create_bucket(bucket_name, region)