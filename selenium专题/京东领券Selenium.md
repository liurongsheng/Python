```python
from time import sleep, time, mktime, strptime, strftime, localtime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import json

TargetTimeInput = "2018-11-15 14:03:00"
TargetTime = mktime(strptime(TargetTimeInput, '%Y-%m-%d %H:%M:%S'))
url_login = 'https://plogin.m.jd.com/user/login.action?appid=300&returnurl=https%3A%2F%2Fwqlogin1.jd.com%2Fpassport%2FLoginRedirect%3Fstate%3D140060197%26returnurl%3Dhttps%253A%252F%252Fpro.m.jd.com%252Fmall%252Factive%252FLU6CDCkfsHiC9udoD6BDcRdcHmT%252Findex.html%253Futm_source%253Dkong%2526utm_medium%253Dzssc%2526utm_campaign%253Dt_1000027277_102033%2526utm_term%253D1095a63f-1680-45e2-8fdf-7e46a574f02f-p_1999-pr_1383-at_102033%2526jd_pop%253D1095a63f-1680-45e2-8fdf-7e46a574f02f%2526abt%253D0&source=wq_passport'
url = 'https://coupon.m.jd.com/center/getCouponCenter.action?batchStr=00000&categoryId=0'

def printCountTime(str, num):
    for i in range(num):
        print("%s %s 秒" % (str, num - i))
        sleep(1)

def clickTarget(driver):
    driver.get(url)
    # driver.find_element_by_xpath("//div[@class='nav']//a[@class='arrow']").send_keys(Keys.ENTER) # 选择下拉箭头
    driver.find_element_by_link_text('发现好店').send_keys(Keys.ENTER) # 选择支付白条
    sleep(3)
    # clickTarget = driver.find_element_by_xpath("//span[contains(text(),'手机话费充值商品')]").find_element_by_xpath(".//..")
    # driver.find_elements_by_class_name("coupon_default_inner")[2].click()

    js = 'document.getElementsByClassName("coupon_default_inner")[2].click()'
    print(driver.execute_script(js))
    sleep(3)

    clickAction = ActionChains(driver)
    clickAction.move_to_element(clickTarget).click_and_hold().perform()
    clickAction.move_to_element(clickTarget).click().send_keys(Keys.ENTER).perform()

    print("抢券一次！")
    # sleep(3)
    # print(clickTarget.tag_name)
    # clickAction = ActionChains(driver)
    # clickAction.move_to_element(clickTarget).click_and_hold().perform()
    # clickAction.move_to_element(clickTarget).send_keys(Keys.ENTER).perform()
    sleep(300)

    # except:
    #     print("脚本出错了！")
    #     driver.close()


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
    sleep(1)
    with open('cookie.txt', 'r') as oldCookie:
        if len(oldCookie) > 1:
            oldCookie = json.loads(oldCookie.read())

    if len(oldCookie)>1:
        for c in oldCookie:
            driver.add_cookie(c)
        print("准备使用cookie登录！")
        clickTarget(driver)
    else:
        driver.find_element_by_xpath("//input[@id='username']").send_keys("397149375@qq.com")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("密码")
        sleep(1)
        driver.find_element_by_id('loginBtn').click()
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
