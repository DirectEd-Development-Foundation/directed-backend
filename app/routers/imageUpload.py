from fastapi import FastAPI, HTTPException
from typing import Dict
import boto3
import os

app = FastAPI()

AWS_REGION = 'us-east-1'
AWS_BUCKET_NAME = 'prideimages'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

s3 = boto3.client('s3', region_name=AWS_REGION,
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  config=boto3.session.Config(signature_version='s3v4'))

def generate_signed_url(key, expiration=60):
    try:
        response = s3.generate_presigned_url('put_object',
                                            Params={'Bucket': AWS_BUCKET_NAME, 'Key': key},
                                            ExpiresIn=expiration,
                                            HttpMethod='PUT')
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating signed URL: {e}")

@app.get('/generate-upload-url', response_model=Dict[str, str])
def generate_upload_url():
    try:
        raw_bytes = os.urandom(16)
        image_name = raw_bytes.hex()

        signed_url = generate_signed_url(image_name)

        if signed_url:
            return {'upload_url': signed_url}
        else:
            raise HTTPException(status_code=500, detail='Failed to generate signed URL')
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in generating upload URL: {e}")
