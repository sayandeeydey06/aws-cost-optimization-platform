from agent.aws_agent import ask_agent

response = ask_agent(
    "Show my EC2 instances"
)

print(response)