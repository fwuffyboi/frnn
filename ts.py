from twitter_scraper_selenium import scrap_profile
import json
import os

usernameFile = open("usernames.txt", "r")
usernameCount = 0

os.chdir("C:\\Users\\User1\\Desktop\\PROJECT_FRNN\\content_got")

for username in usernameFile:

    currentUsername = username
    usernameCount += 1

    currentUsernameLink = f"https://twitter.com/@{currentUsername}"
    print(f"{str(usernameCount)}.{currentUsername}{currentUsernameLink}")

    scrapedInfo = scrap_profile(twitter_username=str(currentUsername), output_format="json", browser="firefox")

    scrapedInfo = json.loads(scrapedInfo)

    for k, v in scrapedInfo.items():
        print(v["content"])
        # contentFileName = currentUsername + "-CONTENT.txt"
        # contentFile = open(contentFileName, "w+")
        # contentFile.writelines(v["content"])
        # contentFile.close()
