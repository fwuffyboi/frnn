import twitterscraper


usernameFile = open("usernames.txt", "r")
lineDone = 0

for line in usernameFile:

	current_username = line	
	lineDone += 1
	
	print("line: " + str(lineDone) + "\n\n")
	list_of_tweets = twitterscraper.query_user_info(user="fwuffyboi")
	
	#print the retrieved tweets to the screen:
	for tweet in list_of_tweets:
		print(tweet)
