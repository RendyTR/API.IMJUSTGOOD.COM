from justgood import imjustgood

api     = imjustgood("INSERT_YOUR_APIKEY_HERE")
data    = api.youtube("friends")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Title : {}".format(data["result"]["title"])
result += "\nAuthor : {}".format(data["result"]["author"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nWatc : {}\n".format(data["result"]["watched"])
result += "\nDesc :\n{}\n".format(data["result"]["description"])
result += "\nThumb :\n{}\n".format(data["result"]["thumbnail"])
result += "\nAudio :\n{}\n".format(data["result"]["audioUrl"])
result += "\nVideo :\n{}\n".format(data["result"]["videoUrl"])
result += "\nPage : {}".format(data["result"]["pageUrl"])
print(result)
