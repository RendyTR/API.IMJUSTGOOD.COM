from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.instastory("the.autobots_corp")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "ID : {}".format(data["result"]["id"])
result  +=  "\nFullname : {}".format(data["result"]["fullname"])
result  +=  "\nUsername : {}".format(data["result"]["username"])

result  +=  "\n\nStories Content :\n"

for i in range(len(data["result"]["stories"])):

    main  =  data["result"]["stories"][i]

    result  +=  "\n{}. {}".format((i+1), main["created"])

    if main["type"] == "image":
        result  +=  "\nImage URL : {}\n".format(main["url"])

    if main["type"] == "video":
        result  +=  "\nVideo URL : {}".format(main["url"])
        result  +=  "\nThumbnail URL : {}\n".format(main["thumbnail"])

result  +=  "\nPicture URL : {}".format(data["result"]["picture"])
result  +=  "\nProfile URL : {}".format(data["result"]["profile"])

print(result)