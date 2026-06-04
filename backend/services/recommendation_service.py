from services.ec2_service import get_ec2_instances
from services.ebs_service import get_unattached_volumes
from services.s3_service import get_s3_buckets
from services.ai_service import generate_ai_recommendation


def get_recommendations():

    recommendations = []

    # EC2 Recommendations
    instances = get_ec2_instances()

    for instance in instances:

        cpu = instance["cpu_utilization"]

        if cpu < 5:

            try:
                ai_text = generate_ai_recommendation(instance)
            except Exception:
                ai_text = "AI recommendation unavailable"

            recommendations.append({
                "resource": "EC2",
                "instance_id": instance["instance_id"],
                "instance_type": instance["instance_type"],
                "recommendation": "Idle EC2 Instance",
                "action": "Consider stopping or downsizing",
                "cpu_utilization": cpu,
                "estimated_savings": "$7.5/month",
                "ai_recommendation": ai_text
            })

    # EBS Recommendations
    volumes = get_unattached_volumes()

    for volume in volumes:

        recommendations.append({
            "resource": "EBS",
            "volume_id": volume["volume_id"],
            "recommendation": "Unattached EBS Volume",
            "action": "Delete unused volume",
            "estimated_savings": "$2/month"
        })

    # S3 Recommendations
    buckets = get_s3_buckets()

    if len(buckets) > 3:

        recommendations.append({
            "resource": "S3",
            "recommendation": "Multiple S3 Buckets Detected",
            "action": "Review unused buckets and enable lifecycle policies",
            "estimated_savings": "$1-$5/month"
        })

    return recommendations