from twitter_scraper_selenium import scrap_profile

usernameFile = open("usernames.txt", "r")
lineDone = 0

for currentUsername in usernameFile:

	url = f"https://twitter.com/@{currentUsername}/"

	lineDone += 1

	scraped = scrap_profile(twitter_username="twitter", browser="firefox")
	print(scraped)
	# print("Completed: " + str(lineDone))
