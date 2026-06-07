import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def lambda_tool():

    client = boto3.client(
        "lambda",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    response = client.list_functions()

    functions = []

    for func in response["Functions"]:

        functions.append({
            "name": func["FunctionName"],
            "runtime": func.get("Runtime", "Unknown"),
            "memory": func["MemorySize"]
        })

    return functions