from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.youtube("friends")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Title : {}".format(data["result"]["title"])
result += "\nAuthor : {}".format(data["result"]["author"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nWatched : {}\n".format(data["result"]["watched"])
result += "\nDescription :\n{}\n".format(data["result"]["watched"])
result += "\nThumbnail :\n{}\n".format(data["result"]["thumbnail"])
result += "\nAudio :\n{}\n".format(data["result"]["audioUrl"])
result += "\n\nVideo :\n{}".format(data["result"]["videoUrl"])
result += "\n\nPage : {}".format(data["result"]["pageUrl"])
print(result)
