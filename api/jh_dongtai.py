#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode
#----------------------------------
# 航班动态调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/20
#----------------------------------

def main():

    #配置您申请的APPKey
    appkey = "e17516f1bef436cb0fda6e9efd7f45e9"

    #1.城市列表
    request1(appkey,"GET")

    #2.航班查询(新)
    request2(appkey,"GET")

    #3.机场简介
    request3(appkey,"GET")

    #4.航线查询
    request4(appkey,"GET")



#城市列表
def request1(appkey, m="GET"):
    url = "http://apis.juhe.cn/plan/city"
    params = {
        "dtype" : "", #返回类型，如：json 或者 xml（默认json）

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

#航班查询(新)
def request2(appkey, m="GET"):
    url = "http://apis.juhe.cn/plan/snew"
    params = {
        "name" : "", #航班号，如:CZ3869
        "key" : appkey, #APP KEY
        "date" : "", #请求时间，如：2012-12-27 （默认当天时间）
        "dtype" : "", #返回类型，如：json 或者 xml（默认json）
 
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

#机场简介
def request3(appkey, m="GET"):
    url = "http://apis.juhe.cn/plan/airport"
    params = {
        "code" : "", #机场国际三字编码，如:FUG
        "key" : appkey, #APP KEY
        "dtype" : "", #返回类型，如：json 或者 xml（默认json）

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

#航线查询
def request4(appkey, m="GET"):
    url = "http://apis.juhe.cn/plan/bc"
    params = {
        "start" : "", #起飞城市(urlencode),如：北京 或 PEK
        "end" : "", #到达城市,如：上海浦东 或 PVG
        "key" : appkey, #APP KEY
        "date" : "", #请求时间，如：2015-07-27 （默认当天时间）
        "dtype" : "", #返回类型，如： json 或 xml （默认json）

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
