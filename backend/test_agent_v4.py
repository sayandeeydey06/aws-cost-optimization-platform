from agent.aws_agent_v2 import llm_with_tools, tool_map

question = "What is my AWS monthly cost?"

response = llm_with_tools.invoke(question)

if response.tool_calls:

    tool_name = response.tool_calls[0]["name"]

    tool = tool_map[tool_name]

    tool_result = tool.invoke({})

    final_prompt = f"""
    User Question:
    {question}

    Tool Result:
    {tool_result}

    Explain the result and give recommendations.
    """

    final_answer = llm_with_tools.invoke(final_prompt)

    print(final_answer.content)

else:
    print(response.content)