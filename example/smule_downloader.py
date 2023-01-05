from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.smuledl("https://www.smule.com/p/1998769355_3429377039")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Artist : {}".format(data["result"]["artist"])
result  +=  "\nTitle : {}".format(data["result"]["title"])
result  +=  "\nCaption : {}".format(data["result"]["caption"])
result  +=  "\nCreated : {}".format(data["result"]["created"])
result  +=  "\nLove : {}".format(data["result"]["loves"])
result  +=  "\nGift : {}".format(data["result"]["gifts"])
result  +=  "\nListen : {}".format(data["result"]["listens"])
result  +=  "\nComment : {}".format(data["result"]["comments"])
result  +=  "\nType : {}".format(data["result"]["type"])

if data["result"]["type"] == "video":

    result += "\nThumbnail URL : {}".format(data["result"]["thumbnail"])
    result += "\nVideo URL : {}".format(data["result"]["mp4Url"])

result += "\nAudio URL : {}".format(data["result"]["mp3Url"])

print(result)