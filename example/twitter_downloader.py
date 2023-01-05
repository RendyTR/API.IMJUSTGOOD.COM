from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.twitterdl("https://twitter.com/rendytr_/status/1608894312703758336")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Username : {}".format(data["result"]["user"]["username"])
result  +=  "\nFullname : {}".format(data["result"]["user"]["fullname"])
result  +=  "\nLike : {}".format(data["result"]["likes"])
result  +=  "\nQuotes : {}".format(data["result"]["quotes"])
result  +=  "\nReplies : {}".format(data["result"]["replies"])
result  +=  "\nRetweet : {}".format(data["result"]["retweet"])

if data["result"]["videoUrl"] != None:

    result += "\nDuration : {}".format(data["result"]["videoDuration"])
    result += "\nViews : {}".format(data["result"]["videoViews"])
    result += "\nVideo URL : {}".format(data["result"]["videoUrl"])
    result += "\nThumbnail URL : {}".format(data["result"]["videoThumb"])

if data["result"]["imageUrl"] != []:

    result  +=  "\nImage URL : "

    for i in range(len(data["result"]["imageUrl"])):

        result  +=  "\n{}. {}".format((i+1), data["result"]["imageUrl"][i])

result  +=  "\nCaption : {}".format(data["result"]["caption"])
result  +=  "\nCreated : {}".format(data["result"]["created"])
result  +=  "\nPicture URL : {}".format(data["result"]["user"]["avatar"])

print(result)