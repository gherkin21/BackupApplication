import backupmodule

if __name__ == '__main__':
    args = backupmodule.get_args()
    # upload_blob(args.bucket, args.file, args.prefix)
    backupmodule.upload_blob(args.bucket, args.file, "qwerty")
