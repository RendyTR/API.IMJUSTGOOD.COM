from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.joox("lathi")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Singer : {}".format(data["result"]["singer"])
result  +=  "\nTitle : {}".format(data["result"]["title"])
result  +=  "\nAlbum : {}".format(data["result"]["album"])
result  +=  "\nDuration : {}".format(data["result"]["duration"])
result  +=  "\nFilesize : {}".format(data["result"]["size"])
result  +=  "\nM4a URL : {}".format(data["result"]["m4aUrl"])
result  +=  "\nMp3 URL : {}".format(data["result"]["mp3Url"])
result  +=  "\nThumbnail URL : {}".format(data["result"]["thumbnail"])

print(result)