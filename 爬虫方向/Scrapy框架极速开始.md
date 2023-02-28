# Scrapy框架极速开始

scrapy startproject sina // 新建项目

scrapy genspider sinaSC "weibo.com/?category=99991" // 新建爬虫模板，指定爬取网站

修改浏览器请求头等设置

```
ROBOTSTXT_OBEY = False
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
```

scrapy.cfg 同级目录新建start.py开始命令脚本

````
from scrapy import cmdline

cmdline.execute("scrapy crawl sinaSC".split())
````
