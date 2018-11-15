为了提高 selenium 脚本的执行速度，考虑使用 PhantomJS 这类的 Headless 浏览器
Chrome "无界面"(headless)  mac 和 linux 环境要求 Chrome 版本是59+，而 windows 版本的 Chrome 要求是60+

```
from selenium import webdriver

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver_path = r"d:\gitHub\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

    driver.get('https://www.baidu.com/')
    print(driver.title)
```
