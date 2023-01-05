from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.twitter("rendytr_")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "\nID : {}".format(data["result"]["id"])
result  +=  "\nUsername : {}".format(data["result"]["username"])
result  +=  "\nFullname : {}".format(data["result"]["fullname"])
result  +=  "\nVerified : {}".format(data["result"]["verified"])
result  +=  "\nPrivate : {}".format(data["result"]["private"])
result  +=  "\nBiography : {}".format(data["result"]["biography"])
result  +=  "\nTweet : {}".format(data["result"]["tweet"])
result  +=  "\nMedia : {}".format(data["result"]["media"])
result  +=  "\nLike : {}".format(data["result"]["like"])
result  +=  "\nFollowers : {}".format(data["result"]["follower"])
result  +=  "\nFollowing : {}".format(data["result"]["following"])
result  +=  "\nFollowing : {}".format(data["result"]["joined"])
result  +=  "\nLocation : {}".format(data["result"]["location"])
result  +=  "\nWebsite : {}".format(data["result"]["website"])
result  +=  "\nPinned : {}".format(data["result"]["location"])
result  +=  "\nPicture URL : {}".format(data["result"]["avatar"])
result  +=  "\nBanner URL : {}".format(data["result"]["banner"])

pageurl  =  "https://twitter.com/{}".format(data["result"]["username"])

if data["result"]["pinned"] != []:

	result  +=  "\n\nPinned Tweet :"

	for i in range(len(data["result"]["pinned"])):

        main     =  data["result"]["pinned"]

		result  +=  "\n{}. {}/status/{}".format((i+1), pageurl, main[i])

print(result)