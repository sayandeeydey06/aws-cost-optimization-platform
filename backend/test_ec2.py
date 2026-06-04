import boto3
import os
from dotenv import load_dotenv

load_dotenv()

ec2 = boto3.client(
    "ec2",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"])
        print(instance["State"]["Name"])
        print(instance["InstanceType"])