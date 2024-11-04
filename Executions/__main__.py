import sys
import json
import Executor

filepath = sys.argv[1]

with open(filepath, 'r') as file:
    service = json.load(file)

    """Categorizing the requirements like Authorization, Operations, etc..."""
    config = service['s3']
    data = config['authentication']
    scan = config['scanner']
    read = config['reader']

    """Reading data of authentication Section"""
    buckets = config['buckets']
    region = data['region']
    endpoint = data['endpoint']
    access_key_id = data.get("access_key_id", None)
    secret_access_key = data.get("secret_access_key", None)
    session_token = data.get("session_token", None)

    """Reading data of Scanner Sections"""
    is_listed = scan['recursive_listing']
    is_scanned = scan['list_scanned_metadata']

    """Reading data of Reader Operations"""
    max_buffer = read['max_buffer_size']
    row_limit = read['row_limit']
    pages = read['pages']
    skip_file_above_size = read['skip_file_above_size']
    skip_file_type = read['skip_file_type']

    for bucket in buckets:

        """Authentication initialized with S3Executor"""
        s3_execution = Executor.S3Executor(bucket, region, endpoint, access_key_id, secret_access_key, session_token)

        """Sample File generation"""
        s3_execution.load_sample()
        print("\tSample data loaded!")

        """Scanner operations"""
        if is_listed is True:
            s3_execution.list_directory()
        if is_scanned:
            s3_execution.discover()

        """Reading the file listed"""
        s3_execution.read_all(max_buffer, pages, row_limit, skip_file_above_size, skip_file_type)
