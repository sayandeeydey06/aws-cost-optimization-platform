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
3 actionable recommendations maximum.

## Estimated Savings
If applicable.
"""
    final_answer = llm.invoke(final_prompt)

    return {
    "answer": final_answer.content,
    "tool_used": tool_name
}

