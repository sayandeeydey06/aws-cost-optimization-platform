from services.ec2_service import get_ec2_instances
from services.ebs_service import get_unattached_volumes
from services.pricing_service import get_monthly_cost


def get_recommendations():

    recommendations = []

    # EC2 Recommendations
    instances = get_ec2_instances()

    for instance in instances:

        cpu = instance["cpu_utilization"]

        if cpu < 5:

            monthly_cost = get_monthly_cost(
                instance["instance_type"]
            )

            recommendations.append({
                "resource": "EC2",
                "instance_id": instance["instance_id"],
                "instance_type": instance["instance_type"],
                "recommendation": "Idle EC2 Instance",
                "action": "Consider stopping or downsizing",
                "cpu_utilization": cpu,
                "estimated_savings": f"${monthly_cost}/month"
            })

    # EBS Recommendations
    volumes = get_unattached_volumes()

    for volume in volumes:

        recommendations.append({
            "resource": "EBS",
            "volume_id": volume["volume_id"],
            "size_gb": volume["size_gb"],
            "recommendation": "Delete unattached volume",
            "action": "Volume is not attached to any EC2 instance",
            "estimated_savings": "$1-$5/month"
        })

    return recommendations