# Introduction #
`TweetScraper` can get tweets from [Twitter Search](https://twitter.com/search-home). It surpasses 31192 maximum tweets of [twitter API ](https://developer.twitter.com/). This project is originated from [TweetScraper](https://github.com/jonbakerfish/TweetScraper) and added some functionality within the CLI. The main functionaity is resume capability and multi process crawling that are very usefull for large tweet crawling.  
It is built on [Scrapy](http://scrapy.org/) without using [Twitter's APIs](https://dev.twitter.com/rest/public).
The crawled data is not as *clean* as the one obtained by the APIs, but the benefits are you can get rid of the API's rate limits and restrictions. Ideally, you can get all the data from Twitter Search.

**WARNING:** please be polite and follow the [crawler's politeness policy](https://en.wikipedia.org/wiki/Web_crawler#Politeness_policy).
 

# Installation #
It requires [Scrapy](http://scrapy.org/) and [langdetect](https://pypi.python.org/pypi/langdetect?)  Setting up:

    $ git clone https://github.com/sentalysa/TweetScraper
    $ cd TweetScraper/
    $ pip install -r requirements.txt  #add '--user' if you are not root
	$ scrapy list
	$ #If the output is 'TweetScraper', then you are ready to go.

# Usage #
1. In the root folder of this project, run command like: 

		
		python run.py [--outputFilename OUTPUTFILENAME] [--query QUERY]
              [--lang LANG] [--since SINCE] [--until UNTIL]
              [--fromAccount FROMACCOUNT] [--toAccount TOACCOUNT]
              [--maxTweets MAXTWEETS]
              [--numberOfConcurrentCrawler NUMBEROFCONCURRENTCRAWLER]
              [--textOnly True/False] [--configFile CONFIGFILE]

	The *query* can be any thing (keyword, hashtag, etc.) you want to search in [Twitter Search](https://twitter.com/search-home). `TweetScraper` will crawl the search results of the query and save the tweet content. There are several arguments that mentioned above for customizing search, such as *lang*: for lanugage of tweet texts, *since*, and *until*: for time date period selection, *fromAccount* and *toAccount* for getting tweets from or replying to a specified account respectively, *maxTweets* for getting a specific number of tweets, *textOnly* is a boolean option if you want to get just the text of tweets, and *numberOfConcurrentCrawler* for setting number of concurrent crawler for crawling. All the above arguments can be set in a config file and give it to the cli with *configFile* option. e.g.:  
`python run.py --query foo --textOnly True`

2. The tweets will be saved to disk in `./Data/tweet/`. The file format is JSON. Change the `SAVE_TWEET_PATH`  in `TweetScraper/settings.py` if you want another location.

# About #
Sentalysa, part of [Faraadid](https://github.com/Faraadid), focuses on NLP projects using deep learning methods.  
:email: sentalysa@gmail.com
