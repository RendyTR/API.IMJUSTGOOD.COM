from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.facebookdl("https://facebook.com/thejustgood/videos/718603069654361/")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Author : {}".format(data["result"]["author"])
result  +=  "\nID : {}".format(data["result"]["profileId"])
result  +=  "\nDesc : {}".format(data["result"]["caption"])
result  +=  "\nLikes : {}".format(data["result"]["likes"])
result  +=  "\nLoves : {}".format(data["result"]["loves"])
result  +=  "\nShare : {}".format(data["result"]["share"])
result  +=  "\nViews : {}".format(data["result"]["views"])
result  +=  "\nComments : {}".format(data["result"]["comments"])
result  +=  "\nVideo URL : {}".format(data["result"]["videoUrl"])
result  +=  "\nThumbnail URL : {}".format(data["result"]["thumbnail"])

print(result)