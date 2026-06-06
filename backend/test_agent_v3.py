from agent.aws_agent_v2 import llm_with_tools

response = llm_with_tools.invoke(
    "What is my AWS monthly cost?"
)

if response.tool_calls:

    tool_name = response.tool_calls[0]["name"]

    print("Tool Selected:", tool_name)

else:
    print(response.content)