from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

from tools.cost_tool import cost_tool
from tools.ec2_tool import ec2_tool
from tools.ebs_tool import ebs_tool
from tools.s3_tool import s3_tool


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def ask_agent(question: str):

    question_lower = question.lower()

    if "cost" in question_lower or "bill" in question_lower:
        data = cost_tool()

    elif "ec2" in question_lower or "instance" in question_lower:
        data = ec2_tool()

    elif "ebs" in question_lower or "volume" in question_lower:
        data = ebs_tool()

    elif "s3" in question_lower or "bucket" in question_lower:
        data = s3_tool()

    else:
        data = {
            "message": "No matching AWS tool found."
        }

    prompt = f"""
    User Question:
    {question}

    AWS Data:
    {data}

    Explain this data in a simple cloud engineer friendly way.
    Give recommendations if applicable.
    """

    response = llm.invoke(prompt)

    return response.content