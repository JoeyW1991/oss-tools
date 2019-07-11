# /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os, sys, getopt
import oss2

access_key_id = os.getenv("ACCESS_KEY_ID")
access_key_secret = os.getenv("ACCESS_KEY_SECRET")
bucket_name = os.getenv("BUCKET_NAME")
endpoint = os.getenv("ENDPOINT", "oss-cn-shanghai-internal.aliyuncs.com")
object_name = os.getenv("OBJECT_NAME")

num_threads = os.getenv("NUM_THREADS", 4)
num_threads = int(num_threads)

auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, endpoint, bucket_name)


def main(argv):
    opts, args = getopt.getopt(argv,"f:")
    for opt, arg in opts:
        if opt == '-f':
            object_name = arg
    local_file = object_name.split('/')[-1]
    local_file = os.getenv("LOCALE_FILE", local_file)
    oss2.resumable_download(bucket, object_name, local_file, num_threads=num_threads)

if __name__ == "__main__":
    main(sys.argv[1:])
