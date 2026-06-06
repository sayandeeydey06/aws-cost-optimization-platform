from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

from tools.cost_tool import cost_tool
from tools.ec2_tool import ec2_tool
from tools.ebs_tool import ebs_tool
from tools.s3_tool import s3_tool


@tool
def aws_cost():
    """Get current AWS monthly cost."""
    return str(cost_tool())


@tool
def aws_ec2():
    """Get EC2 instances."""
    return str(ec2_tool())


@tool
def aws_ebs():
    """Get unattached EBS volumes."""
    return str(ebs_tool())


@tool
def aws_s3():
    """Get S3 buckets."""
    return str(s3_tool())


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

tools = [
    aws_cost,
    aws_ec2,
    aws_ebs,
    aws_s3
]

tool_map = {
    "aws_cost": aws_cost,
    "aws_ec2": aws_ec2,
    "aws_ebs": aws_ebs,
    "aws_s3": aws_s3,
}

llm_with_tools = llm.bind_tools(tools)