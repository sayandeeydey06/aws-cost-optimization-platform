from services.ebs_service import get_unattached_volumes


def ebs_tool():
    return str(get_unattached_volumes())