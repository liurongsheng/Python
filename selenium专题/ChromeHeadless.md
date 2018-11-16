# ChromeHeadless

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

    driver.get('https://www.baidu.com')
    print(driver.title)
```

## 常用配置

- 禁用图片
`options.add_argument('blink-settings=imagesEnabled=false')`

- 代理
`options.add_argument("--proxy-server=http://" + ip：port)`

- 修改User-Agent
Chrome Headless模式为什么要修改User-Agent, 来看一下同一个浏览器不同模式下的User-Agent：
```
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/62.0.3202.89 Safari/537.36"
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
# 修改User-Agent
chrome_options.add_argument('user-agent= '你想修改成的User-Agent')
```
- 打开新的标签页，节省浏览器打开的时间
js='window.open("https://www.baidu.com");'
driver.execute_script(js)
 
- 关闭新打开的标签页
```
1.获取标签页的句柄
handlesList = driver.window_handles  # 返回一个浏览器中所有标签的句柄列表， 顺序为打开窗口的顺序

2. 切换窗口， 关闭标签
driver.switch_to.window(handlesList[0]) # 切换到百度标签
driver.close()    # 关闭标签，这里必须用 driver.close() ，用driver.quit()会导致浏览器关闭
```

driver 使用完之后切记要 driver.quit()，不然或导致内存爆满

