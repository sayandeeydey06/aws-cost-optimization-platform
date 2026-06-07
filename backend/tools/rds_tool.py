import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def rds_tool():

    rds = boto3.client(
        "rds",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    response = rds.describe_db_instances()

    databases = []

    for db in response["DBInstances"]:
        databases.append({
            "identifier": db["DBInstanceIdentifier"],
            "engine": db["Engine"],
            "status": db["DBInstanceStatus"],
            "class": db["DBInstanceClass"]
        })

    return databases