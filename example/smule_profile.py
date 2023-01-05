from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.smule("avamax")

print(data)

# EXAMPLE GET PROFILE ATTRIBUTES

result   =  "Account Id : {}".format(data["result"]["accountId"])
result  +=  "\nUsername : {}".format(data["result"]["username"])
result  +=  "\nFullname : {}".format(data["result"]["fullname"])
result  +=  "\nBiography : {}".format(data["result"]["biography"])
result  +=  "\nLocation : {}".format(data["result"]["location"])
result  +=  "\nFollowers : {}".format(data["result"]["followers"])
result  +=  "\nFollowing : {}".format(data["result"]["following"])
result  +=  "\nRecording : {}".format(data["result"]["recording"])
result  +=  "\nVIP : {}".format(data["result"]["vip"])
result  +=  "\nVerified : {}".format(data["result"]["verified"])

if data["result"]["post"] != []:

    perform = data["result"]["post"]
    result += "\n\nLast Performances :\n"

    for i in range(len(perform)):

        result += "{}. {}\n".format((i+1), perform[i]["title"])

result  +=  "\nPicture URL : {}".format(data["result"]["pictureUrl"])
result  +=  "\nProfile URL : {}".format(data["result"]["profileUrl"])

print(result)

# EXAMPLE GET LAST PERFORMANCES ATTRIBUTES

number   =  1
result   =  "Not found"

if data["result"]["post"] != []:

    main     =  data["result"]["post"][number-1]
    data     =  api.smuledl(main["pageUrl"])

    result   =  "Artist : {}".format(main["artist"])
    result  +=  "\nTitle : {}".format(main["title"])
    result  +=  "\nCaption : {}".format(main["caption"])
    result  +=  "\nCreated : {}".format(main["created"])
    result  +=  "\nLove : {}".format(main["loves"])
    result  +=  "\nGift : {}".format(main["gifts"])
    result  +=  "\nListen : {}".format(main["listens"])
    result  +=  "\nPerformance : {}".format(main["performances"])
    result  +=  "\nComment : {}".format(data["result"]["comments"])
    result  +=  "\nAudio URL : {}".format(data["result"]["mp3Url"])

    if data["result"]["type"] == "video":
        result += "\nVideo URL : {}".format(data["result"]["mp4Url"])

    result  +=  "\nThumbnail URL: {}".format(main["thumbnail"])
    result  +=  "\nPage URL: {}".format(main["pageUrl"])

print(result)