from justgood import imjustgood

api      =  imjustgood("INSER_YOUR_APIKEY_HERE")
data     =  api.linestore()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "{}".format(data["result"]["title"])
result  +=  "\nAuthor : {}".format(data["result"]["author"])
result  +=  "\nType : {}".format(data["result"]["type"])
result  +=  "\nPrice : {}".format(data["result"]["price"])
result  +=  "\nDecription : {}\n\n".format(data["result"]["desc"])

for x in data["result"]["previews"]:

    if x["content"] == "static":

        result  +=  "- Image URL : {}\n".format(x["image"])

    if x["content"] == "animation":

        result  +=  "- Animation URL : {}\n".format(x["animation"])

    if x["content"] == "popup":

        result  +=  "- Popup URL : {}\n".format(x["popup"])

    if x["sound"] != None:

        result  +=  "- Sound URL : {}\n".format(x["sound"])

result  +=  "\nThumbnail URL : {}".format(data["result"]["thumbnail"])
result  +=  "\nPage URL : {}".format(data["result"]["pageUrl"])

print(result)