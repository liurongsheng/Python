<http://selenium-release.storage.googleapis.com/index.html?path=3.141/>

下载 jar 包 selenium-server-standalone-3.141.59

同时把 chrome 的驱动 chromedriver.exe 放在 jar 包同级目录下

运行 java -jar selenium-server-standalone-3.141.59

C:\>java -jar selenium-server-standalone-3.141.59.jar
00:08:59.520 INFO [GridLauncherV3.parse] - Selenium server version: 3.141.59, revision: e82be7d358
00:08:59.633 INFO [GridLauncherV3.lambda$buildLaunchers$3] - Launching a standalone Selenium Server on port 4444
2018-11-18 00:08:59.710:INFO::main: Logging initialized @510ms to org.seleniumhq.jetty9.util.log.StdErrLog
00:08:59.942 INFO [WebDriverServlet.<init>] - Initialising WebDriverServlet
00:09:00.344 INFO [SeleniumServer.boot] - Selenium Server is up and running on port 4444

网页地址访问 <http://localhost:4444/> 点击 console 来到管理中心 <http://localhost:4444/wd/hub/static/resource/hub.html>

Create Session --》 Load Script

import requests
import json
url = 'http://127.0.0.1:4444/wd/hub/session/'
data = json.dumps({
  "capabilties":{
    "browserName": "chrome"
  }
})
session = requests.post(url, data).json()['sessionId']
base_url = url + session

get_url = base_url + "/url"
get_url_data = json.dumps({
   "url" : "http://www.baidu/com"
})
requests.post(get_url, get_url_data)
