# 京东领券Request版

京东有保护，点击太快了会保护，目测在 应该是 5 秒每次

```
神券到手还要 10 秒
神券到手还要 9 秒
神券到手还要 8 秒
神券到手还要 7 秒
神券到手还要 6 秒
神券到手还要 5 秒
神券到手还要 4 秒
神券到手还要 3 秒
神券到手还要 2 秒
神券到手还要 1 秒
抢券时间终于到了，火速抢券！
jQuery2782959({"message":"只有Plus正式期会员、试用期会员才能领取哟~","code":"30","success":false})
jQuery2782959({"message":"抢得太快了，臣妾做不到啊~","code":"103","success":false})
jQuery2782959({"message":"抢得太快了，臣妾做不到啊~","code":"103","success":false})
jQuery2782959({"message":"抢得太快了，臣妾做不到啊~","code":"103","success":false})
```

```
import requests
from time import sleep, time, mktime, strptime, strftime, localtime

TargetTimeInput = "2018-11-14 23:23:30"
TargetTime = mktime(strptime(TargetTimeInput, '%Y-%m-%d %H:%M:%S'))

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
couponUrl = 'https://a.jd.com/indexAjax/getCoupon.html?callback=jQuery2782959&key=7c6672151d133a2105864c0d0846e670b1fbf20af133741ab7bcd6f4037de38500012079b2f10767a4a6c7ed6ac37e34&type=1&_=1542205175323'
# 领券链接 a 标签上的属性 rel="046be9f2f3bd0c04cad8f7bff04793f83b33bd65618a028e15f4c0a209ae6ea6af47eb4485db5727c10a2574b3976323" 就是 key 值 

referer = 'https://a.jd.com/'
 
getCouponNum = 100 # 抢券次数
getCouponInterval = 500  # 抢券间隔单位毫秒  1000毫秒 = 1秒

def printCountTime(str, num):
    for i in range(num):
        print("%s %s 秒" % (str, num - i))
        sleep(1)

def get_cookie():
    with open("cookie.txt") as f:
        cookies = {}
        for line in f.read().split(';'):
            name, value = line.strip().split('=', 1)
            cookies[name] = value
        return cookies

session = requests.Session()
session.headers['User-Agent'] = user_agent
session.headers['Referer'] = referer
session.cookies = requests.utils.cookiejar_from_dict(get_cookie())

def getCoupon(getCouponNum, getCouponInterval):
    for i in range(getCouponNum):
        result = session.get(couponUrl)
        print(result.text)
        sleep(getCouponInterval/1000)

if __name__ == '__main__':

    CountTime = int(TargetTime - time())
    print("抢券目标时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(TargetTime)) )
    print("当前时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(time())) )
    while CountTime > 60:
        print("抢券倒计时：%s 分 %s 秒" % (CountTime // 60, CountTime % 60))
        CountTime = CountTime - 1
        sleep(1)

    if CountTime < 0:
        print("抢券时间已经到了，火速抢券！")
        getCoupon(getCouponNum, getCouponInterval)
    else:
        print("时间不到3分钟了，准备抢券！")
        while True:
            if(CountTime < 0):
                print("抢券时间终于到了，火速抢券！")
                getCoupon(getCouponNum, getCouponInterval)

            printCountTime("神券到手还要", CountTime)
            CountTime = -1

```
