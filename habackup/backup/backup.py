from os import path
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, prefix, credentials=None):
    """Uploads a file to the bucket."""
    if credentials is not None:
        storage_client = storage.Client.from_service_account_json(credentials)
    else:
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