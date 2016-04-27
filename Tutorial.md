接口地址：http://op.juhe.cn/flight/sav
支持格式：json/xml
请求方式：http get/post
请求示例：http://op.juhe.cn/flight/sav?key=APPKEY&orgCity=SHA&dstCity=NKG&flightdate=2014-12-15&airline=ALL&direct=true&eticket=true
接口备注：国内为主，可查部分国外
调用样例及调试工具：API测试工具
请求参数说明：
名称	类型	必填	说明
 	key	string	是	应用APPKEY(应用详细页查询)
 	dtype	string	否	返回数据的格式,xml或json，默认json
 	orgCity	string	是	始发城市的三字码
 	dstCity	string	是	到达城市的三字码
	flightDate	Date	是	日期（年月日）
 	airline	string	否	航空公司的两字码或者"ALL"或者""
 	direct	boolean	是	直航/转飞
 	eticket	boolean	是	是否必须是电子票
返回参数说明：
名称	类型	说明
 	flightNo	字符串	本航段的航班编号
 	orgCity	字符串	本航段的始发城市的三字码
 	dstcity	字符串	本航段的到达城市的三字码
 	orgAirportTerminal	字符串	本航段的始发机场的航站楼
 	dstAirportTerminal	字符串	本航段的到达机场的航站楼
 	depDate	日期类型	本航段的起飞日期(年月日)
 	depTime	字符串	本航段的起飞时刻（时分）
 	depTimeModify	字符串	本航段的起飞日期修正（＋1表示起飞日期是查询日期的下一天）
 	arrDate	日期类型	本航段的到达日期（年月日）
 	arrTime	字符串	本航段的到达时刻（时分）
 	arrTimeModify	字符串	本航段的到达日期修正（＋1表示到达日期是查询日期的下一天）
 	flightTime	字符串	飞行时间，单位：分钟
 	asr	布尔型	本航段的ASR支持标志
 	isEtkt	布尔型	本航段的电子票标志
 	link	字符串	本航段的连接级别
 	meal	布尔型	本航段的餐食标志
 	planeStyle	字符串	本航段使用的机型
 	stopNumber	长整型	本航段的经停次数
 	isCodeShare	布尔型	本航段的代码共享标志
 	carrier	字符串	代码共享航段的真实承运人
 	punctualityRate	浮点型	本航班最近1个月的参考准点率
 	source	字符型	根据outstyle标记返回所需要的内容
 	AirportTax	字符串	机建费
 	fuelTax	字符串	燃油费
 	PriceFare	货币	最低票面价
 	costFare	货币	成本价
 	CabinName	字符串	本舱位的名称
 	CabinInfo	字符串	本舱位的座位信息，A表示剩余座位大于9，数字是表示剩余座位数其他请参看航信订座手册。
 	Fare	货币	票面价
 	AirportFee	货币	机场建设费
 	OilFee	货币	燃油附加费
 	Cost	货币	成本价 = 票面价*(1-返点%)
 	PolicyCode	字符串	政策ID
 	discountRate	字符串	折扣
 	Points	浮点	返点
 	basicCabinType	字符串	基础舱位

JSON返回示例：
{
    "resultcode": "200",
    "reason": "Success",
    "result": {
        "AVResult": [
            {
                "IBE_Flights": {
                    "IBE_Flight": {
                        "FlightNO": "QF4045",
                        "orgCity": "PVG",
                        "dstcity": "NKG",
                        "depDate": "2014-12-15T00:00:00",
                        "depTime": "2150",
                        "depTimeModify": [],
                        "arrDate": "2014-12-15T00:00:00",
                        "arrtime": "2250",
                        "arrTimeModify": [],
                        "asr": "true",
                        "isEtkt": "true",
                        "link": "DS",
                        "meal": "true",
                        "planeStyle": "319",
                        "stopNumber": "0",
                        "isCodeShare": "true",
                        "Cabin": [],
                        "carrier": "MU2882",
                        "OrgAirportTerminal": "T1",
                        "DstAirportTerminal": "T2",
                        "FlightTime": "1:00",
                        "PunctualityRate": [],
                        "AirportTax": "50",
                        "fuelTax": "30",
                        "PriceFare": "0",
                        "costFare": "880"
                    }
                }
            },
            {
                "IBE_Flights": {
                    "IBE_Flight": {
                        "FlightNO": "CZ9685",
                        "orgCity": "PVG",
                        "dstcity": "NKG",
                        "depDate": "2014-12-15T00:00:00",
                        "depTime": "2150",
                        "depTimeModify": [],
                        "arrDate": "2014-12-15T00:00:00",
                        "arrtime": "2250",
                        "arrTimeModify": [],
                        "asr": "true",
                        "isEtkt": "true",
                        "link": "DS",
                        "meal": "true",
                        "planeStyle": "319",
                        "stopNumber": "0",
                        "isCodeShare": "true",
                        "Cabin": [],
                        "carrier": "MU2882",
                        "OrgAirportTerminal": "T1",
                        "DstAirportTerminal": "T2",
                        "FlightTime": "1:00",
                        "PunctualityRate": [],
                        "AirportTax": "50",
                        "fuelTax": "30",
                        "PriceFare": "0",
                        "costFare": "880"
                    }
                }
            },
            {
                "IBE_Flights": {
                    "IBE_Flight": {
                        "FlightNO": "MU2882",
                        "orgCity": "PVG",
                        "dstcity": "NKG",
                        "depDate": "2014-12-15T00:00:00",
                        "depTime": "2150",
                        "depTimeModify": [],
                        "arrDate": "2014-12-15T00:00:00",
                        "arrtime": "2250",
                        "arrTimeModify": [],
                        "asr": "true",
                        "isEtkt": "true",
                        "link": "DS",
                        "meal": "true",
                        "planeStyle": "319",
                        "stopNumber": "0",
                        "isCodeShare": "false",
                        "Cabin": {
                            "IBE_Cabin": [
                                {
                                    "CabinName": "F",
                                    "CabinInfo": "5",
                                    "FD_Info": {
                                        "Fare": "1940",
                                        "PolicyCode": "头等舱",
                                        "discountRate": "220",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "F"
                                    }
                                },
                                {
                                    "CabinName": "Y",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "880",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "100",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "B",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "870",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "99",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "M",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "790",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "90",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "E",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "700",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "80",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "H",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "660",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "75",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "K",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "620",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "70",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "L",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "570",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "65",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "N",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "530",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "60",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "R",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "440",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "50",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "S",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "400",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "45",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                },
                                {
                                    "CabinName": "V",
                                    "CabinInfo": "A",
                                    "FD_Info": {
                                        "Fare": "350",
                                        "PolicyCode": "经济舱",
                                        "discountRate": "40",
                                        "AirportFee": "50",
                                        "OilFee": "30",
                                        "Cost": "0",
                                        "basicCabinType": "Y"
                                    }
                                }
                            ]
                        },
                        "carrier": [],
                        "OrgAirportTerminal": "T1",
                        "DstAirportTerminal": "T2",
                        "FlightTime": "1:00",
                        "PunctualityRate": "64",
                        "AirportTax": "50",
                        "fuelTax": "30",
                        "PriceFare": "350",
                        "costFare": "880"
                    }
                }
            }
        ],
        "Fareprice": {
            "AirportTax": "50",
            "fuelTax": "30",
            "Price": "350",
            "cost": "880"
        }
    },
    "error_code": 0
}
