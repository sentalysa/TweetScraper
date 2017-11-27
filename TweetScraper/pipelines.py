# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy.exceptions import CloseSpider
import logging
import json
import os
from scrapy import crawler
from subprocess import call
from TweetScraper.items import Tweet, TextTweet
from TweetScraper.utils import mkdirs
import sys
# from scrapy.contrib.closespider import CloseSpider


logger = logging.getLogger(__name__)

class SaveToFilePipeline(object):
    ''' pipeline that save data to disk '''
    def __init__(self):
        self.saveTweetPath = settings['SAVE_TWEET_PATH']
        self.tweet_counts = 0
        mkdirs(self.saveTweetPath) # ensure the path exists


    def process_item(self, item, spider):
        if isinstance(item, Tweet):
            savePath = os.path.join(self.saveTweetPath, settings['OUTPUT_FILENAME'])
            # self.save_to_file(item, savePath)
            # print("-----------------" + item)
            if(bool(settings['TEXT_ONLY'])):
                tweet = TextTweet()
                tweet['ID'], tweet['text'] = item['ID'], item['text']
                self.save_to_file(tweet, savePath)
            else:
                self.save_to_file(item, savePath)
        else:
            logger.info("Item type is not recognized! type = %s" %type(item))


    def save_to_file(self, item, fname):
        ''' input: 
                item - a dict like object
                fname - where to save
        '''
        with open(fname,'a', encoding='utf8') as f:
            json.dump(dict(item), f, ensure_ascii=False)
            f.write('\n')
        self.tweet_counts += 1
        if(self.tweet_counts == int(settings['MAX_TWEETS'])):
            call(['kill', '9', '%d'%os.getpid()])
            

