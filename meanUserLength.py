usernameFile = open("usernames.txt", "r")

chars = 0
charsList = []

for username in usernameFile:
	for character in username:
		
		charsList += "1"

		if character == " ":
			chars -= 1
		
		print(charsList)
		# print(character)
