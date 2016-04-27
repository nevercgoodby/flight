package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

//----------------------------------
// 航班时刻票价查询调用示例代码 － 聚合数据
// 在线接口文档：http://www.juhe.cn/docs/96
//----------------------------------

/*
代码描述：基于Python的航班时刻票价查询接口调用代码实例
关联数据：航班时刻票价查询
接口地址：http://www.juhe.cn/docs/api/id/96
*/

const APPKEY = "*******************" //您申请的APPKEY

func main() {

	//1.航班可售舱位及价格查询
	Request1()

	//2.航班经停地及起降时间查询
	Request2()

	//3.机票号对应的信息查询
	Request3()

	//4.航班时刻表查询
	Request4()

	//5.票价查询
	Request5()

	//6.特价票查询
	Request6()

	//7.机场/城天气预报
	Request7()

	//8.航空公司规定退改签查询
	Request8()

}

//1.航班可售舱位及价格查询
func Request1() {
	//请求地址
	juheURL := "http://op.juhe.cn/flight/sav"

	//初始化参数
	param := url.Values{}

	//配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
	param.Set("key", APPKEY)    //应用APPKEY(应用详细页查询)
	param.Set("dtype", "")      //返回数据的格式,xml或json，默认json
	param.Set("orgCity", "")    //始发城市的三字码
	param.Set("dstCity", "")    //到达城市的三字码
	param.Set("flightDate", "") //日期（年月日）
	param.Set("airline", "")    //航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;
	param.Set("direct", "")     //直航/转飞
	param.Set("eticket", "")    //是否必须是电子票

	//发送请求
	data, err := Get(juheURL, param)
	if err != nil {
		fmt.Errorf("请求失败,错误信息:\r\n%v", err)
	} else {
		var netReturn map[string]interface{}
		json.Unmarshal(data, &netReturn)
		if netReturn["error_code"].(float64) == 0 {
			fmt.Printf("接口返回result字段是:\r\n%v", netReturn["result"])
		}
	}
}

//2.航班经停地及起降时间查询
func Request2() {
	//请求地址
	juheURL := "http://op.juhe.cn/flight/ff"

	//初始化参数
	param := url.Values{}

	//配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
	param.Set("key", APPKEY)    //应用APPKEY(应用详细页查询)
	param.Set("dtype", "")      //返回数据的格式,xml或json，默认json
	param.Set("flightNo", "")   //航班编号
	param.Set("flightDate", "") //日期（年月日）

	//发送请求
	data, err := Get(juheURL, param)
	if err != nil {
		fmt.Errorf("请求失败,错误信息:\r\n%v", err)
	} else {
		var netReturn map[string]interface{}
		json.Unmarshal(data, &netReturn)
		if netReturn["error_code"].(float64) == 0 {
			fmt.Printf("接口返回result字段是:\r\n%v", netReturn["result"])
		}
	}
}

//3.机票号对应的信息查询
func Request3() {
	//请求地址
	juheURL := "http://op.juhe.cn/flight/detr"

	//初始化参数
	param := url.Values{}

	//配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
	param.Set("key", APPKEY)  //应用APPKEY(应用详细页查询)
	param.Set("dtype", "")    //返回数据的格式,xml或json，默认json
	param.Set("ticketNo", "") //机票号（XXX-XXXXXXXX XXXXXXXXXXX均可）

	//发送请求
	data, err := Get(juheURL, param)
	if err != nil {
		fmt.Errorf("请求失败,错误信息:\r\n%v", err)
	} else {
		var netReturn map[string]interface{}
		json.Unmarshal(data, &netReturn)
		if netReturn["error_code"].(float64) == 0 {
			fmt.Printf("接口返回result字段是:\r\n%v", netReturn["result"])
		}
	}
}

//4.航班时刻表查询
func Request4() {
	//请求地址
	juheURL := "http://op.juhe.cn/flight/sk"

	//初始化参数
	param := url.Values{}

	//配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
	param.Set("key", APPKEY)    //应用APPKEY(应用详细页查询)
	param.Set("dtype", "")      //返回数据的格式,xml或json，默认json
	param.Set("orgCity", "")    //始发城市的三字码
	param.Set("dstCity", "")    //到达城市的三字码
	param.Set("flightDate", "") //日期（年月日）
	param.Set("airline", "")    //航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;
	param.Set("direct", "")     //直航/转飞
	param.Set("nostop", "")     //是否经停

	//发送请求
	data, err := Get(juheURL, param)
	if err != nil {
		fmt.Errorf("请求失败,错误信息:\r\n%v", err)
	} else {
		var netReturn map[string]interface{}
		json.Unmarshal(data, &netReturn)
		if netReturn["error_code"].(float64) == 0 {
			fmt.Printf("接口返回result字段是:\r\n%v", netReturn["result"])
		}
	}
}

//5.票价查询
func Request5() {
	//请求地址
	juheURL := "http://op.juhe.cn/flight/fd"

	//初始化参数
	param := url.Values{}

	//配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
	param.Set("key", APPKEY)    //应用APPKEY(应用详细页查询)
	param.Set("dtype", "")      //返回数据的格式,xml或json，默认json
	param.Set("orgCity", "")    //始发城市的三字码
	param.Set("dstCity", "")    //到达城市的三字码
	param.Set("flightDate", "") //日期（年月日）
	param.Set("airline", "")    //航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;
	param.Set("planeModel", "") //机型(未找到机型的以干线机型处理)
	param.Set("passType", "")   //旅客类型(&quot;AD&quot;：成人；&quot;IN&quot;：婴儿；&quot;CH&quot;：儿童)

	//发送请求
	data, err := Get(juheURL, param)
	if err != nil {
		fmt.Errorf("请求失败,错误信息:\r\n%v", err)
	} else {
		var netReturn map[string]interface{}
		json.Unmarshal(data, &netReturn)
		if netReturn["error_code"].(float64) == 0 {
			fmt.Printf("接口返回result字段是:\r\n%v", netReturn["result"])
		}
	}
}

//6.特价票查询
func Request6() {
	//请求地址
	juheURL := "http://op.juhe.cn/flight/nfd"

	//初始化参数
	param := url.Values{}

	//配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
	param.Set("key", APPKEY)    //应用APPKEY(应用详细页查询)
	param.Set("dtype", "")      //返回数据的格式,xml或json，默认json
	param.Set("orgCity", "")    //始发城市的三字码
	param.Set("dstCity", "")    //到达城市的三字码
	param.Set("flightDate", "") //日期（年月日）
	param.Set("airline", "")    //航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;

	//发送请求
	data, err := Get(juheURL, param)
	if err != nil {
		fmt.Errorf("请求失败,错误信息:\r\n%v", err)
	} else {
		var netReturn map[string]interface{}
		json.Unmarshal(data, &netReturn)
		if netReturn["error_code"].(float64) == 0 {
			fmt.Printf("接口返回result字段是:\r\n%v", netReturn["result"])
		}
	}
}

//7.机场/城天气预报
func Request7() {
	//请求地址
	juheURL := "http://op.juhe.cn/flight/wf"

	//初始化参数
	param := url.Values{}

	//配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
	param.Set("key", APPKEY)  //应用APPKEY(应用详细页查询)
	param.Set("dtype", "")    //返回数据的格式,xml或json，默认json
	param.Set("cityCode", "") //该城市的三字代码
	param.Set(" ", "")        //

	//发送请求
	data, err := Get(juheURL, param)
	if err != nil {
		fmt.Errorf("请求失败,错误信息:\r\n%v", err)
	} else {
		var netReturn map[string]interface{}
		json.Unmarshal(data, &netReturn)
		if netReturn["error_code"].(float64) == 0 {
			fmt.Printf("接口返回result字段是:\r\n%v", netReturn["result"])
		}
	}
}

//8.航空公司规定退改签查询
func Request8() {
	//请求地址
	juheURL := "http://op.juhe.cn/flight/nfn"

	//初始化参数
	param := url.Values{}

	//配置请求参数,方法内部已处理urlencode问题,中文参数可以直接传参
	param.Set("key", APPKEY)    //应用APPKEY(应用详细页查询)
	param.Set("dtype", "")      //返回数据的格式,xml或json，默认json
	param.Set("orgCity", "")    //始发城市的三字码
	param.Set("dstCity", "")    //到达城市的三字码
	param.Set("flightDate", "") //日期（年月日）
	param.Set("airline", "")    //航空公司的两字码或者&quot;ALL&quot;或者&quot;&quot;
	param.Set("cabin", "")      //舱位
	param.Set(" ", "")          //

	//发送请求
	data, err := Get(juheURL, param)
	if err != nil {
		fmt.Errorf("请求失败,错误信息:\r\n%v", err)
	} else {
		var netReturn map[string]interface{}
		json.Unmarshal(data, &netReturn)
		if netReturn["error_code"].(float64) == 0 {
			fmt.Printf("接口返回result字段是:\r\n%v", netReturn["result"])
		}
	}
}

// get 网络请求
func Get(apiURL string, params url.Values) (rs []byte, err error) {
	var Url *url.URL
	Url, err = url.Parse(apiURL)
	if err != nil {
		fmt.Printf("解析url错误:\r\n%v", err)
		return nil, err
	}
	//如果参数中有中文参数,这个方法会进行URLEncode
	Url.RawQuery = params.Encode()
	resp, err := http.Get(Url.String())
	if err != nil {
		fmt.Println("err:", err)
		return nil, err
	}
	defer resp.Body.Close()
	return ioutil.ReadAll(resp.Body)
}

// post 网络请求 ,params 是url.Values类型
func Post(apiURL string, params url.Values) (rs []byte, err error) {
	resp, err := http.PostForm(apiURL, params)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	return ioutil.ReadAll(resp.Body)
}
