# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag
import qiniu.config
for i in range(29749, 42628):
    print(i)
    access_key = 'G7GrXOsaOVXkdHRUiYCcKPCuN8e719D53d6JXw3E'
    secret_key = 'VFuwqdjmor0HKvSUGBLYFTaTUsCxXNwImLTEpnNZ'
    q = Auth(access_key, secret_key)
    bucket = 'hualu'
    key = '/app/user/avatar/{page}.jpg'.format(page=i)
    token = q.upload_token(bucket, key, 3600)
    localfile = '/Users/lydia/projects/a/{page}.jpg'.format(page=i)
    ret, info = put_file(token, key, localfile)
    # print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)