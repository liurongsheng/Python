```python
from time import sleep, time, mktime, strptime, strftime, localtime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
targetText = '海尔净饮水旗舰店'
isTest = True

import json

TargetTimeInput = "2018-12-10 14:03:00"
TargetTime = mktime(strptime(TargetTimeInput, '%Y-%m-%d %H:%M:%S'))
url_login = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9WfGAYk&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
url = 'https://detail.tmall.com/item.htm?id=583478109165&price=1&price=1&sourceType=item&sourceType=item&sourceType=item&sourceType=item&suid=5ff85466-bca4-4e38-890d-2ff973f418c3&suid=5ff85466-bca4-4e38-890d-2ff973f418c3&ut_sk=1.WQQVezaQ5HEDAJwcljCUmcDy_21646297_1544317854678.TaoPassword-WeiXin.1&ut_sk=1.WQQVezaQ5HEDAJwcljCUmcDy_21646297_1544317854678.TaoPassword-WeiXin.1&un=7bd898d431bec789bbeeeafdb2768e28&un=7bd898d431bec789bbeeeafdb2768e28&share_crt_v=1&share_crt_v=1&sp_tk=77%20ldmhUb2JtTkNqenTvv6U=&sp_tk=77%20ldmhUb2JtTkNqenTvv6U=&cpp=1&cpp=1&shareurl=true&shareurl=true&spm=a313p.22.1ol.994368180036&spm=a313p.22.1ol.994368180036&short_name=h.3MsSvN0&short_name=h.3MsSvN0&app=chrome&app=chrome'

def printCountTime(str, num):
    for i in range(num):
        print("%s %s 秒" % (str, num - i))
        sleep(1)

def clickTarget(driver):
    driver.get(url)
    sleep(3)

    driver.find_element_by_link_text('立即购买').send_keys(Keys.ENTER)
    print("抢券一次！")

def loginPageCaptcha(driver):
    try:
        cookies = driver.get_cookies()
        print(cookies)
        with open('cookie.txt', 'w') as cookieFile:
            cookieFile.write(json.dumps(cookies))

        clickTarget(driver)
        # driver.find_element_by_id('captcha')
        # print("找到登录图形码校验，请十秒内完成图形码校验")
        # printCountTime("图形码校验", 10)
        # driver.find_element_by_id('captcha')
    except:
        print("没有登录图形码校验")
        clickTarget(driver)


def get_cookie():
    with open("cookie.txt") as f:
        cookies = {}
        for line in f.read().split(';'):
            name, value = line.strip().split('=', 1)
            cookies[name] = value
        return cookies


def loginPage(driver):
    driver.get(url_login)
    with open('cookie.txt', 'r') as oldCookie:
        cookie = oldCookie.read()
        if len(cookie) > 1:
            cookie = json.loads(cookie)

    if len(cookie)>1:
        for c in cookie:
            driver.add_cookie(c)
        print("准备使用cookie登录！")
        clickTarget(driver)
    else:
        # driver.find_element_by_xpath("//input[@id='username']").send_keys("18750763136")
        # driver.find_element_by_xpath("//input[@id='password']").send_keys("密码")
        # sleep(1)
        # driver.find_element_by_id('btn-submit').click()
        print("登录点击一次，如果没有跳转或者弹出登录图形码校验需要手动辅助")
        printCountTime("登录等待", 10)
        loginPageCaptcha(driver)


if __name__ == '__main__':
    mobileEmulation = {'deviceName': 'iPhone 6'}
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    extension_path = 'd:\gitHub\quan\XPathHelper2.0.2.crx'
    options.add_extension(extension_path)
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    driver_path = r"d:\gitHub\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    # driver.maximize_window()
    CountTime = TargetTime - time()
    print("抢券目标时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(TargetTime)) )
    print("当前时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(time())) )

    if isTest:
        loginPage(driver)
    else:
        print(CountTime)
        while CountTime > 180:
            print("抢券倒计时：%s 分 %s 秒" % (abs(int(CountTime)) // 60, abs(int(CountTime)) % 60))
            CountTime = CountTime - 1
            sleep(1)

        if CountTime < 0:
            print("抢券时间已经到了，火速登录抢券！")
        else:
            print("时间不到3分钟了，跳转去登录抢券！")
        loginPage(driver)
```
