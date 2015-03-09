
import logSetup
if __name__ == "__main__":
	print("Initializing logging")
	logSetup.initLogging()

import TextScrape.TextScrapeBase

import readability.readability
import bs4
import webFunctions
import urllib.error

class Scrape(TextScrape.TextScrapeBase.TextScraper):
	tableKey = 'royalroad'
	loggerPath = 'Main.RoyalRoad.Scrape'
	pluginName = 'RoyalRoadScrape'

	tableName       = "book_western_items"
	changeTableName = "book_western_changes"

	wg = webFunctions.WebGetRobust(logPath=loggerPath+".Web")

	threads = 1

	FOLLOW_GOOGLE_LINKS = False
	allImages = False


	baseUrl = [
		"http://www.royalroadl.com/",
		]
	startUrl = baseUrl

	badwords = [
				"/about/",
				"/join-us/",
				"/chat/",
				'&format=pdf',
				'?format=pdf',
				'?replytocom=',
				"/forum/",
				"/forum",
				"/games/",
				]

	# Content Stripping needs to be determined.
	decomposeBefore = [

	]

	decompose = [

	]

	stripTitle = 'guhehe.TRANSLATIONS |'




def test():
	scrp = GuheheScrape()
	scrp.crawl()
	# scrp.retreiveItemFromUrl(scrp.startUrl)
	# new = gdp.GDocExtractor.getDriveFileUrls('https://drive.google.com/folderview?id=0B-x_RxmzDHegRk5iblp4alZmSkU&usp=sharing')


if __name__ == "__main__":
	test()

