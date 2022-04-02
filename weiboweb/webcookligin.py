# -*- coding:utf-8 -*-
# @Time:2019/6/18
# @Author:wangym
# @Email:123@qq.com
# @File:webcookligin

from selenium import webdriver
import  getcookies
import  time
driver =webdriver.Chrome()
driver.get("https://weibo.com")
tbCookies=getcookies.gettokenweb()
#cook=
# driver.add_cookie({ "name":"Cookie",
#                  "value":'{SINAGLOBAL=4789045886077.128.1533964265475; YF-V5-G0=a5a6106293f9aeef5e34a2e71f04fae4; _s_tentry=login.sina.com.cn; UOR=www.228.com.cn,widget.weibo.com,login.sina.com.cn; Apache=5688356668637.786.1560668654027; ULV=1560668654044:33:4:1:5688356668637.786.1560668654027:1560350543693; wb_view_log_5317798778=1920*10801; Ugrow-G0=9ec894e3c5cc0435786b4ee8ec8a55cc; login_sid_t=e84894f2a6be4721f6762a3db9bd2899; cross_origin_proto=SSL; WBStorage=6b696629409558bc|undefined; wb_view_log=1920*10801; wb_view_log_6910869075=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhiAEVTP0f3w5FO87Rw_VV25JpX5K2hUgL.Foq4eh.4e0McSKM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMc1K541KeNSo-N; ALF=1592205800; SSOLoginState=1560669801; SCF=AqOoUEpU3pPp0BTfcqRmHG_yVubh1Um_R5Bax4TCzB58C1FFdP4WJ9aF_ReFjGubldZnvVSCowxy6Z0owl5Ca4U.; SUB=_2A25wAZ46DeRhGeBH61sY8ynKzjuIHXVTdojyrDV8PUNbmtBeLUXwkW9NQcLKP3k9v9t8nhytSsw5VfKsCH7Ig1eE; SUHB=0oU4zVN4Yag6-d; un=ssfadndsriwaiv-svb@yahoo.com; wvr=6; YF-Page-G0=580fe01acc9791e17cca20c5fa377d00|1560669807|1560669522; wb_view_log_6909937657=1920*10801; weiboNotfication=1379357432380.357; webim_unReadCount=%7B%22time%22%3A1560669823002%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A35%2C%22msgbox%22%3A0%7D"}'})
for cookie in tbCookies:
    driver.add_cookie({
        "domain":".weibo.com",
        "name":cookie,
        "value":tbCookies[cookie],
        "path":'/',
        "expires":None
    })
time.sleep(3)
driver.get("http://weibo.com")
sc='''function forwardWeibo(content, retcode) {
    var formData = new FormData();
    formData.append('pic_src', '');
    formData.append('pic_id', '');
    formData.append('appkey', '');
    formData.append('mid', '4381360821437879');
    formData.append('style_type', 2);
    formData.append('mark', '');
    formData.append('reason', content);
    formData.append('location', 'page_100505_single_weibo');
    formData.append('pdetail', '1005056750452239');
    formData.append('module', '');
    formData.append('page_module_id', '');
    formData.append('refer_sort', '');
    formData.append('rank', 0);
    formData.append('rankid', '');
    formData.append('_t', 0);

    var xhr = new XMLHttpRequest();
    xhr.timeout = 3000;
    xhr.responseType = "text";
    xhr.open('POST', 'https://weibo.com/aj/v6/mblog/forward?ajwvr=6&domain=100505&__rnd=' + new Date().getTime(), true);
    xhr.onload = function(e) {
        if (this.status == 200 || this.status == 304) {
            var data = JSON.parse(this.responseText);
            if (data.code == "100000") {
                // 转发微博成功
                console.log(content);
            } else if (data.code == "100027") {
                // 转发微博失败，需要回答图片验证码的问题
                console.log(data);
            } else {
                // 转发微博失败，其他原因
                console.log(data);
            }
        }
    };
    xhr.send(formData);
}
//forwardWeibo('转发内容');
//forwardWeibo('转发内容',verified('答案'));

// 每5秒转发一次
var count = 1;
var con;
var arry='#王俊凯高能预警#王俊凯#王俊凯高能少年团# 单纯思考简单生活努力坚持俊俊安好@TFBOYS-王俊凯&#王俊凯# #树读[音乐]# #小棉袄[音乐]# 哈哈笑';
var arr = ["[鼓掌]","[good]","[好爱哦]", "[好喜欢]","[可爱]","[太开心]",
"[污]","[嘻嘻]","[爱你]"]; 
var arr1 = ["[抱抱]","[摊手]","[男孩儿]", "[女孩儿]","[可爱]","[太开心]",
"[握手]","[赞]","[兔子]","[熊猫]"]; 


setInterval(function(){
    var index = Math.floor((Math.random()*arr.length)); 
     var index1 = Math.floor((Math.random()*arr1.length)); 
    con=arr[index]+arr1[index1];
    forwardWeibo(con);
}, 10000);'''


driver.execute_script(sc)
time.sleep(40)