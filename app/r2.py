import boto3
import os

s3 = boto3.client(
    "s3",
    endpoint_url=os.environ["R2_ENDPOINT"],
    aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
    region_name="auto",
)

BUCKET = os.environ["R2_BUCKET_NAME"]

def upload_video(file, key):
    s3.upload_fileobj(
        file,
        BUCKET,
        key,
        ExtraArgs={
            "ContentType": file.content_type
        }
    )
