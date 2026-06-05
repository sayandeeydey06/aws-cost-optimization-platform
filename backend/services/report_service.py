from services.aws_cost_service import get_monthly_cost
from services.ec2_service import get_ec2_instances
from services.ebs_service import get_unattached_volumes
from services.s3_service import get_s3_buckets
from services.recommendation_service import get_recommendations


def generate_report():

    cost = get_monthly_cost()

    ec2_instances = get_ec2_instances()

    ebs_volumes = get_unattached_volumes()

    s3_buckets = get_s3_buckets()

    recommendations = get_recommendations()

    total_savings = 0

    for item in recommendations:

        savings = item.get("estimated_savings", 0)

        if isinstance(savings, str):

            savings = savings.replace("$", "")
            savings = savings.replace("/month", "")
            savings = savings.strip()

            # Handle values like "1-5"
            if "-" in savings:
                try:
                    savings = savings.split("-")[-1]
                except:
                    savings = "0"

            try:
                savings = float(savings)
            except:
                savings = 0

        total_savings += savings

    return {
        "monthly_cost": cost,
        "total_ec2_instances": len(ec2_instances),
        "unattached_ebs_volumes": len(ebs_volumes),
        "total_s3_buckets": len(s3_buckets),
        "total_recommendations": len(recommendations),
        "potential_monthly_savings": total_savings,
        "recommendations": recommendations
    }