from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

from services.report_service import generate_report


def create_pdf_report():

    report = generate_report()

    filename = "aws_cost_report.pdf"

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AWS Cost Optimization Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Total EC2 Instances: {report['total_ec2_instances']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Total S3 Buckets: {report['total_s3_buckets']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Potential Savings: ${report['potential_monthly_savings']}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    for rec in report["recommendations"]:

        content.append(
            Paragraph(
                f"{rec['recommendation']} - {rec['action']}",
                styles["Normal"]
            )
        )

    pdf.build(content)

    return filename