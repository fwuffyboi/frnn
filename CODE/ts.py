from twitter_scraper_selenium import scrap_profile
import json
import os

usernameFile = open("../ASSETS/usernames.txt", "r")
usernameCount = 0

os.chdir("/content_got")
printed = ""

for username in usernameFile:

    currentUsername = username
    usernameCount += 1

    currentUsernameLink = f"https://twitter.com/@{currentUsername}"
    print(f"{str(usernameCount)}.{currentUsername}.{currentUsernameLink}")

    scrapedInfo = scrap_profile(twitter_username=str(currentUsername), output_format="json", browser="firefox",
                                tweets_count=1000)

    scrapedInfo = json.loads(str(scrapedInfo))

    for k, v in scrapedInfo.items():
        print(v["content"])
        # printed += f"{username} Completed."
        # printed += v['content'] + "\n"

        # contentFileName = currentUsername + "-CONTENT.txt"
        # contentFile = open(contentFileName, "w+")
        # contentFile.writelines(v["content"])
        # contentFile.close()
