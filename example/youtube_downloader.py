from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.youtubedl("https://youtu.be/POG1xVW-1jQ")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Title : {}".format(data["result"]["title"])
result  +=  "\nAuthor : {}".format(data["result"]["author"])
result  +=  "\nDuration : {}".format(data["result"]["duration"])
result  +=  "\nWatched : {}".format(data["result"]["watched"])
result  +=  "\nDescription : {}".format(data["result"]["watched"])
result  +=  "\nAudio URL : {}".format(data["result"]["audioUrl"])
result  +=  "\nVideo URL : {}".format(data["result"]["videoUrl"])
result  +=  "\nThumbnail URL : {}".format(data["result"]["thumbnail"])
result  +=  "\nPage URL : {}".format(data["result"]["pageUrl"])

print(result)