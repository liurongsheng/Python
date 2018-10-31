BOT_NAME = 'movieSite'

SPIDER_MODULES = ['movieSite.spiders']
NEWSPIDER_MODULE = 'movieSite.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 3
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}

ITEM_PIPELINES = {
   # 'movieSite.pipelines.MovieMySQLPipeline': 100,
   'movieSite.pipelines.MovieMongoDBPipeline': 200,
}

LOG_LEVEL = "WARNING"