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