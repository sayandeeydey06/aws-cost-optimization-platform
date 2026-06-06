from agent.aws_agent_v2 import llm_with_tools

response = llm_with_tools.invoke(
    "What is my AWS monthly cost?"
)

print(response)