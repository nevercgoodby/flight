#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode

#----------------------------------
# 航班实时起降时间调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/99
#----------------------------------

def main():

    #配置您申请的APPKey
    appkey = "*********************"

    #1.实时起降信息查询
    request1(appkey,"GET")

    #2.历史起降信息查询
    request2(appkey,"GET")



#实时起降信息查询
def request1(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/df/fs"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "orgCity" : "", #始发城市的三字码
        "dstCity" : "", #到达城市的三字码
        "flightNo" : "", #航班号
        " " : "", #

    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"

#历史起降信息查询
def request2(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/df/hfs"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "flightNo" : "", #航班号
        "flightDate" : "", #（年月日）

    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"



if __name__ == '__main__':
    main()