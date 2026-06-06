from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

from tools.cost_tool import cost_tool
from tools.ec2_tool import ec2_tool
from tools.ebs_tool import ebs_tool
from tools.s3_tool import s3_tool


# =========================
# AWS TOOLS
# =========================

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


# =========================
# GEMINI MODEL
# =========================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# =========================
# REGISTER TOOLS
# =========================

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


# =========================
# AGENT FUNCTION
# =========================

def ask_agent(question: str):

    response = llm_with_tools.invoke(question)

    # Tool Calling
    if response.tool_calls:

        tool_name = response.tool_calls[0]["name"]

        print(f"\nTool Called: {tool_name}")

        tool = tool_map[tool_name]

        tool_result = tool.invoke({})

        print(f"\nTool Result:\n{tool_result}")

        final_prompt = f"""
You are an AWS Cost Optimization Expert.

User Question:
{question}

AWS Data:
{tool_result}

Provide the answer in the following format:

## Summary

Short explanation.

## Findings

Explain what was discovered.

## Cost Impact

Mention any costs or savings.

## Recommendations

Provide practical AWS recommendations.

## Next Actions

Provide clear next steps.

Keep the answer professional and concise.
"""

        final_answer = llm.invoke(final_prompt)

        return final_answer.content

    # If no tool required
    return response.content