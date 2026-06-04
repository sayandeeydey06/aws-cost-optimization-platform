from services.ai_service import generate_ai_recommendation

instance = {
    "instance_id": "i-test",
    "instance_type": "t3.micro",
    "cpu_utilization": 0.21
}

print(generate_ai_recommendation(instance))