#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, urllib
from urllib import urlencode

def main():
    #配置您申请的APPKey
    appkey = "7f921f1f4a371acc"
    #1.实时起降信息查询
    qijiang(appkey,"GET")

#可售
def keshou(appkey, m="GET"):
    url = "http://api.chuxingdata.com/flight/sav?"
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
    print res, content
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"

#经停地
def jingtingdi(appkey, m="GET"):
    url = "http://api.chuxingdata.com/flight/ff?"
    $params = array(
      "appkey" => $appkey,//应用APPKEY(应用详细页查询)
      "dtype" => "",//返回数据的格式,xml或json，默认json
      "orgCity" => "",//始发城市的三字码
      "dstCity" => "",//到达城市的三字码
      "flightDate" => "",//日期（年月日）
      "airline" => "",//航空公司的两字码或者"ALL"或者""
      "direct" => "",//直航/转飞
      "eticket" => "",//是否必须是电子票
);

#机票号
def jipiaohao(appkey, m="GET"):
    url = "http://api.chuxingdata.com/flight/detr?"

#票价
def piaojia(appkey,m="GET"):
    url = "http://api.chuxingdata.com/flight/fd?"

#退改签
def tuigaiqian(appkey,m="GET"):
    url = "http://api.chuxingdata.com/flight/wf?"

#天气
def weather(appkey, m="GET"):
    url = "http://api.chuxingdata.com/flight/wf?"

#时刻
def shike(appkey, m="GET"):
    url = "http://api.chuxingdata.com/flight/sk?"

#实时起降信息查询
def qijiang(appkey, m="GET"):
    url = "http://api.chuxingdata.com/flight/fs?"
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
    print res, content
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
