#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode

#----------------------------------
# 航班时刻票价查询调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/96
#----------------------------------

"""
代码描述：基于Python的航班时刻票价查询接口调用代码实例
关联数据：航班时刻票价查询
接口地址：http://www.juhe.cn/docs/api/id/96
"""


def main():

    #配置您申请的APPKey
    appkey = "*********************"

    #1.航班可售舱位及价格查询
    request1(appkey,"GET")

    #2.航班经停地及起降时间查询
    request2(appkey,"GET")

    #3.机票号对应的信息查询
    request3(appkey,"GET")

    #4.航班时刻表查询
    request4(appkey,"GET")

    #5.票价查询
    request5(appkey,"GET")

    #6.特价票查询
    request6(appkey,"GET")

    #7.机场/城天气预报
    request7(appkey,"GET")

    #8.航空公司规定退改签查询
    request8(appkey,"GET")



#航班可售舱位及价格查询
def request1(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/sav"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "orgCity" : "", #始发城市的三字码
        "dstCity" : "", #到达城市的三字码
        "flightDate" : "", #日期（年月日）
        "airline" : "", #航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;
        "direct" : "", #直航/转飞
        "eticket" : "", #是否必须是电子票

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

#航班经停地及起降时间查询
def request2(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/ff"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "flightNo" : "", #航班编号
        "flightDate" : "", #日期（年月日）

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

#机票号对应的信息查询
def request3(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/detr"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "ticketNo" : "", #机票号（XXX-XXXXXXXX XXXXXXXXXXX均可）

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

#航班时刻表查询
def request4(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/sk"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "orgCity" : "", #始发城市的三字码
        "dstCity" : "", #到达城市的三字码
        "flightDate" : "", #日期（年月日）
        "airline" : "", #航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;
        "direct" : "", #直航/转飞
        "nostop" : "", #是否经停

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

#票价查询
def request5(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/fd"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "orgCity" : "", #始发城市的三字码
        "dstCity" : "", #到达城市的三字码
        "flightDate" : "", #日期（年月日）
        "airline" : "", #航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;
        "planeModel" : "", #机型(未找到机型的以干线机型处理)
        "passType" : "", #旅客类型(&quot;AD&quot;：成人；&quot;IN&quot;：婴儿；&quot;CH&quot;：儿童)

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

#特价票查询
def request6(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/nfd"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "orgCity" : "", #始发城市的三字码
        "dstCity" : "", #到达城市的三字码
        "flightDate" : "", #日期（年月日）
        "airline" : "", #航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;

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

#机场/城天气预报
def request7(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/wf"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "cityCode" : "", #该城市的三字代码
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

#航空公司规定退改签查询
def request8(appkey, m="GET"):
    url = "http://op.juhe.cn/flight/nfn"
    params = {
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml或json，默认json
        "orgCity" : "", #始发城市的三字码
        "dstCity" : "", #到达城市的三字码
        "flightDate" : "", #日期（年月日）
        "airline" : "", #航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;
        "cabin" : "", #舱位
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



if __name__ == '__main__':
    main()
