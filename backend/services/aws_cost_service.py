import boto3
from dotenv import load_dotenv
import os

load_dotenv()

load_dotenv()

print("ACCESS_KEY =", os.getenv("AWS_ACCESS_KEY_ID"))
print("REGION =", os.getenv("AWS_REGION"))

client = boto3.client(
    "ce",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)


def get_monthly_cost():
    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": "2026-06-01",
            "End": "2026-06-30"
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    amount = response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]

    return {
        "monthly_cost_usd": float(amount)
    }