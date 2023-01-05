from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.instapost("https://www.instagram.com/p/Cg7q-DJBBIw/")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Instagram {}".format(data["result"]["postType"])
result  +=  "\nUsername : {}".format(data["result"]["username"])
result  +=  "\nFullname : {}".format(data["result"]["fullname"])
result  +=  "\nVerified : {}".format(data["result"]["verified"])
result  +=  "\nPrivate : {}".format(data["result"]["private"])
result  +=  "\nCaption : {}".format(data["result"]["caption"])
result  +=  "\nLikes : {}".format(data["result"]["likes"])
result  +=  "\nComments : {}".format(data["result"]["comments"])
result  +=  "\nCreated : {}".format(data["result"]["created"])

result  +=  "\n\nPost Detail :"

for i in range(len(data["result"]["postData"])):

    main  =  data["result"]["postData"][i]

    if main["type"] == "image":
       result  +=  "\n{}. Image URL : {}".format((i+1), main["postUrl"])

    if main["type"] == "video":
       result  +=  "\n{}. Video URL : {}".format((i+1), main["postUrl"])
       result  +=  "\nThumbnail URL : {}".format(main["poster"])

result  +=  "\n\nPicture URL : {}".format(data["result"]["picture"])

print(result)

# LINK SUPPORT FOR TYPE INSTAGRAM POST, TV, REEL, HIGHLIGHTS