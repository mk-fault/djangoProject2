import hashlib
from django.conf import settings

def MD5(ori_data):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(ori_data.encode('utf-8'))
    return obj.hexdigest()