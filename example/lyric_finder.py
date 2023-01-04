from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.lyric("faded")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Title : {}\n".format(data["result"]["title"])
result  +=  "Artist : {}\n\n".format(data["result"]["artist"])
result  +=  "{}\n\n".format(data["result"]["lyric"])
result  +=  "Thumbnail URL : ".format(data["result"]["image"])
print(result)
