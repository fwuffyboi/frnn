from twitter_scraper_selenium import scrap_profile
import json

usernameFile = open("C:\\Users\\User1\\Desktop\\PROJECT-FRNN\\ASSETS\\usernames.txt", "r")


def getTweets():
    currentUsername = username
    print(currentUsername)

    scrapedInfo = scrap_profile(twitter_username=str(currentUsername), output_format="json", browser="firefox",
                                tweets_count=5000)

    scrapedInfo = json.loads(str(scrapedInfo))

    for k, v in scrapedInfo.items():
        print(v["content"])


# printed += f"{username} Completed."
# printed += v['content'] + "\n"


for username in usernameFile:
    try:
        getTweets()

    except:
        getTweets()
