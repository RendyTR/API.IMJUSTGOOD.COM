from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.lyric("faded")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  +=  "Title : {}".format(data["result"]["title"])
result  +=  "\nArtist : {}".format(data["result"]["artist"])
result  +=  "\nLyric : {}".format(data["result"]["lyric"])
result  +=  "\nThumbnail URL : {}".format(data["result"]["image"])

print(result)