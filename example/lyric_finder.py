from justgood import imjustgood

api      =   imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =   api.lyric("faded")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
image    =  data["result"]["image"]
result  +=  "Title : {}\n".format(data["result"]["title"])
result  +=  "Artist : {}\n".format(data["result"]["artist"])
result  +=  "Lyric :\n\n{}".format(data["result"]["lyric"])
print(image, result)
