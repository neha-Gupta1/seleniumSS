import time 
import boto3
from botocore.client import Config

def takeSS(driver,url):
    driver.get(url)
    time.sleep(2)
    driver.save_screenshot("screenshot1.png")
    outputUrl=upload_to_aws("screenshot1.png", 'bucketseleniumfail', "passing1.png")
    driver.quit()
    return outputUrl


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id="******", aws_secret_access_key="*********",config=Config(signature_version='s3v4')) #

    try:
        s3.upload_file(local_file, bucket, s3_file)
    except FileNotFoundError:
        return False
    
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        ExpiresIn=60,
        Params={
            'Bucket': bucket,
            'Key': s3_file
        }
    )
    return url