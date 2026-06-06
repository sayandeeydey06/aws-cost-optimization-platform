from services.ec2_service import get_ec2_instances


def ec2_tool():
    return str(get_ec2_instances())