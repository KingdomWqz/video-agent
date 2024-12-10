# from qiniu.services.storage.uploader import put_file
# from qiniu.utils import etag
# from qiniu.auth import Auth

from qiniu import Auth, put_file, etag
import os

import qiniu.config

def upload_file(localfile):
    #构建鉴权对象
    access_key = os.getenv('QINIU_AK')
    secret_key = os.getenv('QINIU_SK')
    q = Auth(access_key, secret_key)

    #要上传的空间
    bucket_name = 'showhype-test'
    
    #上传后保存的文件名
    key = 'test.mp4'
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    #要上传文件的本地路径
    ret, info = put_file(token, key, localfile, version='v2')
    
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
    
    # 删除本地文件
    if os.path.exists(localfile):
        os.remove(localfile)
        print(f"{localfile} has been deleted.")
    else:
        print(f"{localfile} does not exist.")
    
    return 'http://so7r90nt8.hn-bkt.clouddn.com/' + key