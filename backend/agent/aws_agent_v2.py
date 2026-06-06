def ask_agent(question: str):

    question_lower = question.lower()

    # =========================
    # TOOL ROUTING
    # =========================

    if any(word in question_lower for word in [
        "cost",
        "billing",
        "bill",
        "monthly cost",
        "spending",
        "expense"
    ]):
        tool_name = "aws_cost"

    elif any(word in question_lower for word in [
        "ec2",
        "instance",
        "instances",
        "server"
    ]):
        tool_name = "aws_ec2"

    elif any(word in question_lower for word in [
        "ebs",
        "volume",
        "volumes",
        "disk",
        "storage volume"
    ]):
        tool_name = "aws_ebs"

    elif any(word in question_lower for word in [
        "s3",
        "bucket",
        "buckets"
    ]):
        tool_name = "aws_s3"

    else:
        # fallback to Gemini tool calling
        response = llm_with_tools.invoke(question)

        if response.tool_calls:
            tool_name = response.tool_calls[0]["name"]
        else:
            return response.content

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

1. Answer ONLY what the user asked.
2. Do NOT dump raw AWS data unless specifically requested.
3. Summarize findings.
4. Give cost optimization recommendations.
5. Use markdown formatting.
6. Keep answer under 200 words.

Examples:

Question:
"What is my AWS monthly cost?"

Answer:
## Monthly Cost

Your current AWS monthly cost is approximately $0.00.

## Analysis

You are currently operating within Free Tier limits.

## Recommendation

Continue monitoring usage and configure AWS Budgets alerts.


Question:
"Show my EC2 instances"

Answer:
## EC2 Summary

You currently have 4 running EC2 instances.

All instances are t3.micro and have very low CPU utilization (<1%).

## Cost Optimization

These instances appear underutilized.

## Recommendation

- Stop unused instances
- Schedule non-production instances
- Consider Reserved Instances if long-term usage is expected

Generate the response now.
"""
    final_answer = llm.invoke(final_prompt)

    return final_answer.content