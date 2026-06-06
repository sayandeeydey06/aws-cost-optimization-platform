from services.s3_service import get_s3_buckets


def s3_tool():
    return str(get_s3_buckets())