from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.pinterest("https://pin.it/3yq1n3k")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

for x in data["result"]:

    if x["type"] == "mp4":
        result  = "Type : MP4"
        result += "\nURL : {}".format(x["url"])
        result += "\nThumbnail : {}".format(x["cover"])

    if x["type"] == "gif":
        result  = "Type : GIF"
        result += "\nURL : {}".format(x["url"])

    if x["type"] == "png":
        result  = "Type : PNG"
        result += "\nURL : {}".format(x["url"])

    if x["type"] == "jpg":
        result  = "Type : JPG"
        result += "\nURL : {}".format(x["url"])

    print(result)