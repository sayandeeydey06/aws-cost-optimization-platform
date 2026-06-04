import boto3
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

cloudwatch = boto3.client(
    "cloudwatch",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)


def get_cpu_utilization(instance_id):

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)

    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[
            {
                "Name": "InstanceId",
                "Value": instance_id
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=3600,
        Statistics=["Average"]
    )

    datapoints = response["Datapoints"]

    if not datapoints:
        return 0

    avg_cpu = sum(
        point["Average"]
        for point in datapoints
    ) / len(datapoints)

    return round(avg_cpu, 2)