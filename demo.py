import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
response = s3.create_bucket(
    ACL='private',
    Bucket='awsamit1112',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',

    },

)

try:
    response = s3.upload_file('abc.txt', 'awsamit1112', 'newfile.txt')
except ClientError as e:
    logging.error(e)


print(response)