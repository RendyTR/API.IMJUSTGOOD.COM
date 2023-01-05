from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.snackvideo("https://sck.io/p/owme4gdC")

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "ID : {}".format(data["result"]["profileId"])
result  +=  "\nUsername : {}".format(data["result"]["username"])
result  +=  "\nFullname : {}".format(data["result"]["fullname"])
result  +=  "\nLike : {}".format(data["result"]["like"])
result  +=  "\nShare : {}".format(data["result"]["share"])
result  +=  "\nComment : {}".format(data["result"]["comment"])
result  +=  "\nCaption : {}".format(data["result"]["caption"])
result  +=  "\nCreated : {}".format(data["result"]["created"])
result  +=  "\nPicture URL : {}".format(data["result"]["picture"])
result  +=  "\nVideo URL : {}".format(data["result"]["video"])
result  +=  "\nThumbnail URL : {}".format(data["result"]["thumbnail"])

print(result)
