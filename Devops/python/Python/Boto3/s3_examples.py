import boto3
from dotenv import load_dotenv
import os

load_dotenv()
aws_session = boto3.Session(
    region_name=os.getenv('AWS_REGION_ID'),
    aws_access_key_id=os.getenv('AWS_EC2_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_EC2_SECRET_ACCESS_KEY')
)

s3_client = aws_session.client('s3')


def upload_file_to_s3(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_name
    try:
        response = s3_client.upload_file(file_name, bucket_name, object_name)
        print("File uploaded successfully to S3 bucket.")
    except Exception as e:
        print("Error uploading file to S3:", str(e))


def download_file_from_s3(bucket_name, object_name, file_name):
    try:
        s3_client.download_file(bucket_name, object_name, file_name)
        print("File downloaded successfully from S3 bucket.")
    except Exception as e:
        print("Error downloading file from S3:", str(e))


# Main function
def main():
    #upload_file_to_s3('file1.txt', 'testitd001', 'remote-file1.txt')
    download_file_from_s3('testitd001', 'remote-file1.txt', 'dddddddddddddd.txt')


if __name__ == "__main__":
    main()
