# -*- coding: utf-8 -*-

# 账号配置
# username = "licchuo168"
# password = "111"
username = "zoudong11"
password = "111111"


'''
 刷票参数配置
 座位简写----SW:商务  YD:一等座  ED:二等座 GR:高软 PR:软 DW:动卧 YW:硬卧  YZ:硬座 RZ 软座
'''
# 0：车次优先  1：座位号优先
type = 0

#李长超
persons=["李长超"]

fromStation = "%u676D%u5DDE%2CHZH"#杭州

toStation="%u4E5D%u6C5F%2CJJG"#九江

fromDates=["2018-02-11","2018-02-12","2018-02-13"]

checis=["Z4047","3147","G1461","G1583","G1393"]

zuocis=["ED","YD","GR","YW","YZ"]

#张乔茵
# fromStation = "%u5ECA%u574A%2CLJP"#廊坊
# toStation="%u9526%u5DDE%2CJZD"#锦州
# fromDates=["2018-02-09","2018-02-10","2018-02-11","2018-02-12"]
# checis=["G395","K1301"]
#
# zuocis=["ED","YW"]
#
# persons=["张乔茵"]


'''
 发送信息配置
 qq： 发送qq消息要求已经登陆qq，而且qq的窗口是独立的，现在新版的qq一般都是将所有的聊天窗口聚合在一起，因此要设置将qq窗口分离，或者将需要发送消息的那个窗口单独分离出来。 
 微信：文件助手 to_user='filehelper'
'''
to_user='12306' #用户名

