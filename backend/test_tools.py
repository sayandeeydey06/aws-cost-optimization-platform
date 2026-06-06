from tools.cost_tool import cost_tool
from tools.ec2_tool import ec2_tool
from tools.ebs_tool import ebs_tool
from tools.s3_tool import s3_tool

print("COST:")
print(cost_tool())

print("\nEC2:")
print(ec2_tool())

print("\nEBS:")
print(ebs_tool())

print("\nS3:")
print(s3_tool())