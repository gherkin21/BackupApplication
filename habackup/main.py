from args.args import get_args
from backup.backup import upload_blob

if __name__ == '__main__':
    args = get_args()
    upload_blob(args.bucket, args.file, args.prefix)