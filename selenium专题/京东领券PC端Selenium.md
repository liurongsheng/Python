```python
from time import sleep, time, mktime, strptime, strftime, localtime
from selenium import webdriver
import json

TargetTimeInput = "2018-11-15 14:03:00"
TargetTime = mktime(strptime(TargetTimeInput, '%Y-%m-%d %H:%M:%S'))
url_login = 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
url = 'https://a.jd.com/'
targetText = 'IAM健康电器旗舰店'

def printCountTime(str, num):
    for i in range(num):
        print("%s %s 秒" % (str, num - i))
        sleep(1)

def clickTarget(driver):
    driver.get(url)
    driver.find_element_by_link_text("发现好店").click() # 选择支付白条
    sleep(3)
    clickTarget = driver.find_element_by_xpath("(//span[contains(text(),"+ targetText +")]//..//..//..//div[@class='q-opbtns'])[1]")
    # clickTarget = driver.find_element_by_xpath("((//div[@class='cate-cont']//div)[1]//div[@class='q-opbtns']//span)[1]")
    print(clickTarget.location)
    clickTarget.click()
    sleep(3)
    print("抢券一次！")

def loginPageCaptcha(driver):
    try:
        cookies = driver.get_cookies()
        print(cookies)
        with open('cookie.txt', 'w') as cookieFile:
            cookieFile.write(json.dumps(cookies))

        clickTarget(driver)
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
    sleep(1)
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

        driver.find_element_by_link_text("账户登录").click()
        driver.find_element_by_xpath("//input[@id='loginname']").send_keys("397149375@qq.com")
        driver.find_element_by_xpath("//input[@id='nloginpwd']").send_keys("密码")
        sleep(1)
        driver.find_element_by_id('loginsubmit').click()
        print("登录点击一次，如果没有跳转或者弹出登录图形码校验需要手动辅助")
        printCountTime("登录等待", 10)
        loginPageCaptcha(driver)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_argument("--auto-open-devtools-for-tabs")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    extension_path = 'd:\gitHub\quan\XPathHelper2.0.2.crx'
    options.add_extension(extension_path)
    driver_path = r"d:\gitHub\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    driver.maximize_window()
    CountTime = TargetTime - time()
    print("抢券目标时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(TargetTime)) )
    print("当前时间 %s" % strftime('%Y-%m-%d %H:%M:%S', localtime(time())) )
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
