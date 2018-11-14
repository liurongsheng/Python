```
import requests
from time import sleep, time, mktime, strptime, strftime, localtime

TargetTimeInput = "2018-11-14 19:59:40"
TargetTime = mktime(strptime(TargetTimeInput, '%Y-%m-%d %H:%M:%S'))

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
couponUrl = 'https://a.jd.com/indexAjax/getCoupon.html?callback=jQuery9585449&key=5c596b0bb0c8e51851a885edcd663909e0654d6c428513dec1a5524ce383604eb8936acc369079d28a66e4bdee6fc640&type=1&_=1542195188442'
referer = 'https://a.jd.com/'

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

def getCoupon():
    result = session.get(couponUrl)
    print(result.text)

if __name__ == '__main__':

    CountTime = TargetTime - time()
    print("抢券目标时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(TargetTime)) )
    print("当前时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(time())) )
    while CountTime > 180:
        print("抢券倒计时：%s 分 %s 秒" % (abs(int(CountTime)) // 60, abs(int(CountTime)) % 60))
        CountTime = CountTime - 1
        sleep(1)

    if CountTime < 0:
        print("抢券时间已经到了，火速抢券！")
        getCoupon()
    else:
        print("时间不到3分钟了，准备抢券！")
        while CountTime :
            if(TargetTime - time() < 1):
                print("抢券时间已经到了，火速抢券2！")
                getCoupon()
            printCountTime("抢券", int(CountTime))
```
