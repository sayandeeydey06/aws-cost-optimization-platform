from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_recommendation(instance):

    prompt = f"""
    Analyze this AWS EC2 instance.

    Instance ID: {instance['instance_id']}
    Instance Type: {instance['instance_type']}
    CPU Utilization: {instance['cpu_utilization']}%

    Give a short AWS cost optimization recommendation.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content