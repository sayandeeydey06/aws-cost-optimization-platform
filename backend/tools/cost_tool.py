from services.aws_cost_service import get_monthly_cost


def cost_tool():
    return str(get_monthly_cost())