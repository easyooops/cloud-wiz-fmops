import os
from dotenv import load_dotenv
from boto3.session import Session
from botocore.exceptions import ClientError

class S3Service:
    def __init__(self):
        self.load_credentials()
        self.load_bucket_name()
        self.s3_client = self.create_s3_client()
        self.create_bucket_if_not_exists()

    def load_credentials(self):
        load_dotenv()
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.aws_region = os.getenv("AWS_REGION", "us-east-1")

    def load_bucket_name(self):
        self.bucket_name = os.getenv("AWS_S3_BUCKET_STORE_NAME")

    def create_s3_client(self):
        session = Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region
        )
        s3_client = session.client('s3')
        return s3_client

    def create_bucket_if_not_exists(self):
        try:
            response = self.s3_client.head_bucket(Bucket=self.bucket_name)
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                self.create_bucket()
            else:
                print(e)

    def create_bucket(self):
        try:
            response = self.s3_client.create_bucket(
                Bucket=self.bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': self.aws_region
                }
            )
            return response
        except ClientError as e:
            print(e)
            return None

    def create_directory(self, directory_name: str):
        try:
            response = self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=directory_name + '/'
            )
            return response
        except ClientError as e:
            print(e)
            return None

    def list_objects(self, directory_name: str = ''):
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=directory_name)
            return response.get('Contents', [])
        except ClientError as e:
            print(e)
            return []

    def upload_file(self, file_path: str, key: str):
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, key)
        except ClientError as e:
            print(e)

    def delete_file(self, key: str):
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=key)
        except ClientError as e:
            print(e)

    def delete_bucket(self):
        objects = self.list_objects()
        for obj in objects:
            key = obj['Key']
            self.delete_file(key)
        try:
            response = self.s3_client.delete_bucket(Bucket=self.bucket_name)
            return response
        except ClientError as e:
            print(e)
            return None            