from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

from tools.cost_tool import cost_tool
from tools.ec2_tool import ec2_tool
from tools.ebs_tool import ebs_tool
from tools.s3_tool import s3_tool
from tools.rds_tool import rds_tool
from tools.lambda_tool import lambda_tool


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

@tool
def aws_rds():
    """Get RDS database instances."""
    return str(rds_tool())

@tool
def aws_lambda():
    """Get Lambda functions."""
    return str(lambda_tool())


# =========================
# GEMINI MODEL
# =========================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# =========================
# TOOL REGISTRY
# =========================

tool_map = {
    "aws_cost": aws_cost,
    "aws_ec2": aws_ec2,
    "aws_ebs": aws_ebs,
    "aws_s3": aws_s3,
    "aws_rds": aws_rds,
    "aws_lambda": aws_lambda,
}

# =========================
# TOOL CALLING MODEL
# =========================

llm_with_tools = llm.bind_tools(
    [aws_cost, aws_ec2, aws_ebs, aws_s3, aws_rds]
)


# =========================
# AGENT
# =========================

def ask_agent(question: str):

    question_lower = question.lower()

    # Manual routing first
    if any(word in question_lower for word in [
        "cost", "billing", "bill", "monthly cost",
        "spending", "expense"
    ]):
        tool_name = "aws_cost"

    elif any(word in question_lower for word in [
        "ec2", "instance", "instances", "server"
    ]):
        tool_name = "aws_ec2"

    elif any(word in question_lower for word in [
        "ebs", "volume", "volumes", "disk"
    ]):
        tool_name = "aws_ebs"

    elif any(word in question_lower for word in [
        "s3", "bucket", "buckets"
    ]):
        tool_name = "aws_s3"

    elif any(word in question_lower for word in [
    "rds", "database", "databases", "db"
    ]):
        tool_name = "aws_rds"

    elif any(word in question_lower for word in [
    "lambda",
    "serverless",
    "function",
    "functions"
]):
     tool_name = "aws_lambda"

    else:
        # Let Gemini decide
        response = llm_with_tools.invoke(question)

        if response.tool_calls:
            tool_name = response.tool_calls[0]["name"]
        else:
            return {
                "answer": response.content,
                "tool_used": "none"
            }

    print(f"\nTool Called: {tool_name}")

    tool = tool_map[tool_name]

    tool_result = tool.invoke({})

    print(f"\nTool Result:\n{tool_result}")

    final_prompt = f"""
You are a Senior AWS FinOps Engineer.

User Question:
{question}

AWS Data:
{tool_result}

Rules:
- Use ONLY the AWS data provided.
- Do NOT make assumptions.
- Keep the answer under 200 words.
- Be concise and professional.
- If data is unavailable, clearly say so.

Format:

## Summary
2-3 lines.

## Findings
Bullet points.

## Recommendations
Maximum 3 recommendations.

## Estimated Savings
Only if applicable.
"""

    final_answer = llm.invoke(final_prompt)

    return {
        "answer": final_answer.content,
        "tool_used": tool_name
    }