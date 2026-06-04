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


def get_unattached_volumes():

    response = ec2.describe_volumes()

    volumes = []

    for volume in response["Volumes"]:

        if len(volume["Attachments"]) == 0:

            volumes.append({
                "volume_id": volume["VolumeId"],
                "size_gb": volume["Size"],
                "state": volume["State"]
            })

    return volumes