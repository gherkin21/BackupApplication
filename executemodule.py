import backupmodule

if __name__ == '__main__':
    args = backupmodule.get_args()
    backupmodule.upload_blob(args.bucket, args.file, args.prefix)