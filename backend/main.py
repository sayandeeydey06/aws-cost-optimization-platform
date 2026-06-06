from fastapi import FastAPI
from services.aws_cost_service import get_monthly_cost
from services.ec2_service import get_ec2_instances
from services.recommendation_service import get_recommendations
from services.ebs_service import get_unattached_volumes
from services.s3_service import get_s3_buckets
from services.report_service import generate_report
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from services.pdf_service import create_pdf_report
from pydantic import BaseModel
from agent.aws_agent_v2 import llm_with_tools, tool_map
from agent.aws_agent import ask_agent

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AWS Cost Optimization Agent Running"}

@app.get("/cost")
def cost():
    return get_monthly_cost()

@app.get("/ec2")
def ec2():
    return get_ec2_instances()

@app.get("/recommendations")
def recommendations():
    return get_recommendations()

@app.get("/ebs")
def ebs():
    return get_unattached_volumes()

@app.get("/s3")
def s3():
    return get_s3_buckets()

@app.get("/report")
def report():
    return generate_report()

@app.get("/report/pdf")
def download_report():

    pdf_file = create_pdf_report()

    return FileResponse(
        pdf_file,
        media_type="application/pdf",
        filename="AWS_Cost_Report.pdf"
    )


@app.post("/chat")
def chat(request: ChatRequest):
    response = ask_agent(request.question)

    return {
        "response": response
    }