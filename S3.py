import boto3
import pandas as pd
import io

# some initial variables
bucket_name = "ds-education-la"
object_key = 'NYC_School_Data.xlsx'

# open client
client = boto3.client('s3')


with open("NYC_School_Data.xlsx", "rb") as f:
    data = f.read()
    response = client.put_object(
    Body=data,
    Bucket=bucket_name,
    Key= object_key
)
print("Result of pushing object", response)