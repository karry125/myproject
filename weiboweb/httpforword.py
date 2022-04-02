# -*- coding:utf-8 -*-
# @Time:2019/6/11
# @Author:wangym
# @Email:123@qq.com
# @File:httpforword

import  requests
import getcookies
import time
from urllib import parse
import urllib3
urllib3.disable_warnings() # 取消警告
from random import randint
import json
print(randint(1,1000))
def httpfor():
        url='https://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100505&__rnd='+str(int(time.time()*1000))
        print(url)
        # 居然少了referer就不能转发没有这个也能转发 Content-Type: application/x-www-form-urlencoded
        headers={"Referer":"https://weibo.com/6750452239/Hy8z8623B?type=repost",
                 "Content-Type": "application/x-www-form-urlencoded",
                 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
        cookies = getcookies.gettokenweb()
        data={"pic_src":"","pic_id":"" ,"appkey":"" ,"mid":"4381360821437879","style_type": 2,"mark":"",
              "reason": randint(1,100),"location":"page_100505_single_weibo",
                "pdetail":"1005056750452239",
                "module": "",
                "page_module_id":"",
                "refer_sort":"",
                "rank":0,
                "rankid":"",
                "isReEdit":"",
                "t":0}
        data = parse.urlencode(data)
        print(data)
        # session=requests.session()
        # session.verify=False
        # session.headers=headers
        # ,allow_redirects=False在post里
        cookies ={"Cookie":"SINAGLOBAL=744237330026.5515.1560670462774; wvr=6; YF-V5-G0=7e17aef9f70cd5c32099644f32a261c4; _s_tentry=passport.weibo.com; UOR=,,www.baidu.com; Apache=3519990191630.3335.1560851659687; ULV=1560851659704:2:2:2:3519990191630.3335.1560851659687:1560670462786; login_sid_t=7ae7fba75ebdaf094d414a5d3e7b57b6; cross_origin_proto=SSL; Ugrow-G0=cf25a00b541269674d0feadd72dce35f; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFL-KqjIiCn3H7fdNT0jYGz5JpX5K2hUgL.FoMpS0z01KzReKe2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNeKMEe0.E1h20; SCF=Ap4Lqr-TdEXPwQf0Ipclp2RzoZhPBzEbyVQxZuwu9zhZ3TlvUI57nE98ufOtxbozyc-SLqW9N9Vo5h1D6-lEVCs.; SUB=_2A25wDMalDeRhGeFP7FAS-SzEyj-IHXVTe79trDV8PUNbmtBeLUr9kW9NQRnleHYHjQ5CxMtNuyN6XrMoRxPb5Ffl; SUHB=0G0-a2_AavU1-A; un=vlilmwjtpiukied-wkr457@yahoo.com; wb_view_log_7172392813=1920*10801; WBtopGlobal_register_version=3cccf158e973a877; YF-Page-G0=761bd8cde5c9cef594414e10263abf81|1560852307|1560852301; webim_unReadCount=%7B%22time%22%3A1560852328857%2C%22dm_pub_total%22%3A1%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A27%2C%22msgbox%22%3A0%7D"}
        #cookies ={"Cookie":" YF-V5-G0=95d69db6bf5dfdb71f82a9b7f3eb261a; Ugrow-G0=d52660735d1ea4ed313e0beb68c05fc5; _s_tentry=weibo.com; Apache=744237330026.5515.1560670462774; SINAGLOBAL=744237330026.5515.1560670462774; ULV=1560670462786:1:1:1:744237330026.5515.1560670462774:; wb_view_log_6910869192=1920*10801; wb_view_log_6910869075=1920*10801; login_sid_t=a9ca8dcf0f155c198e246f0df121ddff; cross_origin_proto=SSL; wb_view_log=1920*10801; UOR=,,login.sina.com.cn; wb_view_log_6729110737=1920*10801; WBStorage=6b696629409558bc|undefined; WBtopGlobal_register_version=3cccf158e973a877; SCF=Ap4Lqr-TdEXPwQf0Ipclp2RzoZhPBzEbyVQxZuwu9zhZrhvWmqsyluHMahOi2mkOtHskTx_5yjzjHchOSMexSPg.; SUB=_2A25wAYsFDeRhGeNN6lUW-SbLzDSIHXVTdvvNrDV8PUNbmtBeLRCskW9NScUIHGtbUtqumw89SNp_O3iUmXO_MN8g; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5me5eO.oDT-UKOleuPdzQT5JpX5K2hUgL.Fo-0eKMN1KnNS0n2dJLoI0qLxK-L1-zLBoBLxKnL1hBL1KqLxKBLBonL122LxKML1-2L1hBLxKqL1KqLB-BLxKML1hzLBo.t; SUHB=0ElKClvhmhYt8A; ALF=1561277908; SSOLoginState=1560673109; un=13738056812@139.com; wvr=6; wb_view_log_5317798778=1920*10801; weiboNotfication=1379357432380.357; webim_unReadCount=%7B%22time%22%3A1560673123002%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A3%2C%22allcountNum%22%3A541%2C%22msgbox%22%3A0%7D; YF-Page-G0=e57fcdc279d2f9295059776dec6d0214|1560673126|1560673115"}
        #co={'wb_view_log': '1920*10801', 'WBStorage': '6b696629409558bc|undefined', 'Ugrow-G0': '1ac418838b431e81ff2d99457147068c', 'login_sid_t': '36ab808e48f6132036dd36b91d6d6814', 'cross_origin_proto': 'SSL', 'YF-V5-G0': '8c4aa275e8793f05bfb8641c780e617b', '_s_tentry': 'passport.weibo.com', 'SINAGLOBAL': '4361002427144.5225.1560853501069', 'Apache': '4361002427144.5225.1560853501069', 'ULV': '1560853501080:1:1:1:4361002427144.5225.1560853501069:', 'SUHB': '0KAhyDPSUKR5Bq', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WW5aXQ_axeBlREcO_r0-SR15JpX5K2hUgL.FoMpS0z01KeEShe2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNeKMEe0.0eoB0', 'ALF': '1592389527', 'SSOLoginState': '1560853528', 'SCF': 'AhKh7ALWJlwn_2HP3bHjlnTWm-BHEJHrU9Npk_pZHR42H7qUs7EsxLCawp-AvgRTATDv9SIQ_j94sXikDx4Rw7w.', 'SUB': '_2A25wDMxJDeRhGeFP7FAS-S3Ozz-IHXVTe7qBrDV8PUNbmtBeLXjWkW9NQRnlEkemss9gDeuU83B5lVp3i9THVVRH', 'un': 'szkcebkinlvqavx-nryr4@yahoo.com'}
        try:
           re= requests.post(url,data=data,headers=headers,cookies=cookies)
           #re.encoding="utf-8"
           print(re.text)
           print(re)
           code=re.json()["code"]
           if code == "100000":
                   print("转发成功")
           else:
                print("转发异常",code)
                print(re.json())
           return  code
        except Exception as e:
                raise e
                return re.text
        print(re.status_code,re.json())
        # 1560260847599
# base_url="https://weibo.com"
# params={"pic_src":"","pic_id":"" ,"appkey":"" ,"mid":"4381360821437879","style_type": 2,"mark":"",
#               "reason": randint(1,100),"location":"page_100505_single_weibo",
#                 "pdetail":"1005056750452239",
#                 "module": "",
#                 "page_module_id":"",
#                 "refer_sort":"",
#                 "rank":0,
#                 "rankid":"",
#                 "isReEdit":"",
#                 "t":0}
# url = base_url + parse.urlencode(params)
# print(url)

# for i in range(4):
#         code=httpfor()
#         if code==

httpfor()
i=0
# while i<4:
#         time.sleep(10)
#         code = httpfor(cookies)
#         if code == "100000":
#            i=i+1
#            continue
#         else:
#             break