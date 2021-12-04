import twitter_scraper_selenium
import json
import time

commonKeywordsVar = (
    "fursuit", "furry", "furrys", "furries"
)


def commonKeywords():
    keywords = commonKeywordsVar
    epoch = 20
    epochDone = 0

    for i in range(epoch):
        for wordInKeywords in keywords:
            scrapedInfo = twitter_scraper_selenium.scrap_keyword(keyword=wordInKeywords, browser="firefox",
                                                                 tweets_count=200)
            scrapedInfo = json.loads(str(scrapedInfo))

            for k, v in scrapedInfo.items():
                vContent = v["content"]
                vContent.replace("\n", "")
                print(str(vContent))

        epochDone += 1
        print(f"Epoch {epochDone} complete. Waiting 30 minutes.")

        # wait 30 minutes.
        time.sleep(60 * 30)  # seconds in a minute X minutes to wait.
        print(f"Restarting. Epoch: {epochDone}")


def uncommonKeywords():
    keywords = ("fursuit friday", "fur meet", "MFF", "midwest fur fest", "#MFF",
                "anthrocon")

    epoch = 20
    epochDone = 0

    for i in range(epoch):
        for wordInKeywords in keywords:
            scrapedInfo = twitter_scraper_selenium.scrap_keyword(keyword=wordInKeywords, browser="firefox")
            scrapedInfo = json.loads(str(scrapedInfo))

            for k, v in scrapedInfo.items():
                vContent = v["content"]
                vContent.replace("\n", "")
                print(str(vContent))

        epochDone += 1
        print(f"Epoch {epochDone} complete.")

        # wait 30 minutes.
        time.sleep(60 * 30)  # seconds in a minute X minutes to wait.
        print(f"Restarting. Epoch: {epochDone}")


commonKeywords()
