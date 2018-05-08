# -*- coding: utf-8 -*-
__author__ = 'CL'
__date__ = '2018/3/30 下午3:52'

import hashlib
import re

def get_md5(url):
    if isinstance(url,str):#判断是不是Unicode
        url=url.encode("utf-8")
    m=hashlib.md5()
    m.update(url)
    return m.hexdigest()

# if __name__=="__main__":
#     print(get_md5("http://www.1905.com"))