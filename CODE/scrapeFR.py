from twitter_scraper_selenium import scrap_profile

microsoft = scrap_profile(twitter_username="fwuffyboi",output_format="json",browser="firefox")

ms = open("ms.txt", "w+")
ms.write(microsoft)
ms.close()
print(microsoft['fwuffyboi'][0]['content'])
