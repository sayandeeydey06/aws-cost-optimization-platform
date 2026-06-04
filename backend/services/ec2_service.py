import boto3
from dotenv import load_dotenv
from services.cloudwatch_service import get_cpu_utilization
import os

load_dotenv()

ec2 = boto3.client(
    "ec2",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)


def get_ec2_instances():
    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            cpu = get_cpu_utilization(
    instance["InstanceId"]
)
            
            print(
    "Instance:",
    instance["InstanceId"],
    "CPU:",
    cpu
)
            instances.append({
                "instance_id": instance["InstanceId"],
                "instance_type": instance["InstanceType"],
                "state": instance["State"]["Name"],
                "cpu_utilization": cpu
            })

    return instances