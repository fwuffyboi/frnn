# import the module
import tweepy
  
# assign the values accordingly
consumer_key = "6Hc20xp8MqFVTL4q5zTWVBiAH"
consumer_secret = "LwQu1SDHjhFfRMo3PmEjTrOrgBwxSesSmgURGunCWyqWKH1M9n"
access_token = "1355097383332425729-4jduWpBQbi098JkBlDuR8ZmEGARugm"
access_token_secret = "XQGp9nFRX4ixCjTR259R4jjDrBdXLISt2C3XITWw4zpX8"
  
# authorization of consumer key and consumer secret
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

# calling the api 
api = tweepy.API(auth)

# using get_user with screen_name
screen_namee = "geeksforgeeks"
user = api.get_user(screen_name=screen_namee)
  
# printing the name of the user
print("\nThe screen name " + screen_name +
      " corresponds to the user with the name : " +
      user.name)
