from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.porn("student")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Title : {}".format(data["result"]["title"])
result  +=  "\nDuration : {}".format(data["result"]["duration"])
result  +=  "\nQuality : {}".format(data["result"]["quality"])
result  +=  "\nWatched : {}".format(data["result"]["watched"])
result  +=  "\nVideo URL : {}".format(data["result"]["videoUrl"])
result  +=  "\nThumbnail URL : {}".format(data["result"]["thumbnail"])

print(result)