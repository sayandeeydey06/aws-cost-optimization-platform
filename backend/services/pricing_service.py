INSTANCE_PRICING = {
    "t3.micro": 7.50,
    "t2.micro": 8.00,
    "t3.small": 15.00,
    "t3.medium": 30.00
}


def get_monthly_cost(instance_type):
    return INSTANCE_PRICING.get(instance_type, 0)