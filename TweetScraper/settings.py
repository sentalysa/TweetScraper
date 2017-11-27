# -*- coding: utf-8 -*-
# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = 'TweetScraper'
# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'CRITICAL'
DOWNLOAD_HANDLERS = {'s3': None,} # from http://stackoverflow.com/a/31233576/2297751, TODO
SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    'TweetScraper.pipelines.SaveToFilePipeline':100
}
FEED_EXPORT_ENCODING = 'utf-8'
# settings for where to save data on disk
SAVE_TWEET_PATH = './Data/tweet/'
OUTPUT_FILENAME = 'output.jl'
MONGODB_DB = "TweetScraper"        # database name to save the crawled data
MONGODB_TWEET_COLLECTION = "tweet" # collection name to save tweets


# USER_DEFINED
MAX_TWEETS = "-1"
TEXT_ONLY = "False"

