# importing data
!pip install boto3
from boto3 import client
from boto3.session import Session
from s3_info import *
import pandas as pd
import io

# s3 access
aws_access_key_id = aws_access_key_id
aws_secret_access_key = aws_secret_access_key
aws_default_region = aws_default_region

# collect path string within s3
bucket_name = bucket_name
session = Session(aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)
s3 = session.resource('s3')
your_bucket = s3.Bucket(bucket_name)
path=[s3_file.key for s3_file in your_bucket.objects.all()]

# read out paths to determine which file want
path

# load file as pandas df
s3c = client('s3', region_name = aws_default_region,
                 aws_access_key_id = aws_access_key_id,
                 aws_secret_access_key = aws_secret_access_key)
obj = s3c.get_object(Bucket= bucket_name , Key = path[i])
df = pd.read_csv(io.BytesIO(obj['Body'].read()), encoding='utf8', index_col=0)
