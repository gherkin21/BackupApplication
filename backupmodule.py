import argparse
from os import path
from google.cloud import storage

def get_args():
    # Read arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--credentials', '-c')
    parser.add_argument('--file', '-f', required=True)
    parser.add_argument('--project', '-p', required=True)
    parser.add_argument('--bucket', '-b', required=True)
    parser.add_argument('--prefix', '-P', default=None)
    args = parser.parse_args()
    return args

def upload_blob(bucket_name, source_file_name, prefix):
    """Uploads a file to the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    destination_blob_name = path.basename(source_file_name) if prefix is None else (prefix+"/"+path.basename(source_file_name)).replace("//","/")
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )