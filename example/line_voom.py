from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.timeline("https://linevoom.line.me/post/1165950237762956312")

print(data)

# GET CERTAIN ATTRIBUTES

result   =  "Display name : {}".format(data["result"]["displayName"])
result  +=  "\nLike : {}".format(data["result"]["like"])
result  +=  "\nShare : {}".format(data["result"]["share"])
result  +=  "\nComment : {}".format(data["result"]["comment"])
result  +=  "\nCaption : {}".format(data["result"]["caption"])

if data["result"]["timeline"] != []:

    result  +=  "\n\nTimeline Post :"

    for i in range(len(data["result"]["timeline"])):

        main  =  data["result"]["timeline"][i]

        if main["type"] == "image":

            result  +=  "\n{}. Image URL : {}".format((i+1), main["url"])

        if main["type"] == "video":

            result += "\n{}. Video URL : {}".format((i+1), main["url"])
            result += "\nThumbnail URL : {}".format(main["thumbnail"])

result  +=  "\nPicture URL : {}".format(data["result"]["pictureUrl"])

print(result)