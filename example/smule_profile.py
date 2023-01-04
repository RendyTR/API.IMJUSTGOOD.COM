from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.smule("avamax")
print(data)

# EXAMPLE GET PROFILE ATTRIBUTES

picture  =  data["result"]["pictureUrl"]

result   =  "Account Id : {}\n".format(data["result"]["accountId"])
result  +=  "Username : {}\n".format(data["result"]["username"])
result  +=  "Fullname : {}".format(data["result"]["fullname"])
result  +=  "Biography : {}\n".format(data["result"]["biography"])
result  +=  "Location : {}\n".format(data["result"]["location"])
result  +=  "Followers : {}\n".format(data["result"]["followers"])
result  +=  "Following : {}\n".format(data["result"]["following"])
result  +=  "Recording : {}\n".format(data["result"]["recording"])
result  +=  "VIP : {}\n".format(data["result"]["vip"])
result  +=  "Verified : {}\n".format(data["result"]["verified"])
result  +=  "Profile URL : {}".format(data["result"]["profileUrl"])

if data["result"]["post"] != []:
    result += "\n\nPerformances :"
    for i in range(len(data["result"]["post"])):
        title   = data["result"]["post"][i]["title"]
        result += "\n   {}. {}".format(number+1, title)

print(picture, result)

# EXAMPLE GET PERFORMANCES ATTRIBUTES

select_num    =  1
audio, video  =  None, None
performances  =  data["result"]["post"]
result        =  "Not found"

if performances != []:

    main      =  performances[select_num-1]
    cover     =  main["thumbnail"]
    print(cover)

    data      =  api.smuledl(main["pageUrl"])
    result    =  "Artist : {}\n".format(main["artist"])
    result   +=  "Title : {}\n".format(main["title"])
    result   +=  "Caption : {}\n".format(main["caption"])
    result   +=  "Created : {}\n".format(main["created"])
    result   +=  "Love : {}\n".format(main["loves"])
    result   +=  "Gift : {}\n".format(main["gifts"])
    result   +=  "Listen : {}\n".format(main["listens"])
    result   +=  "Performs : {}\n".format(main["performances"])
    result   +=  "Page URL : {}".format(main["pageUrl"])
    audio     =  data["result"]["mp3Url"]
    if data["result"]["type"] == "video":
        video = data["result"]["mp4Url"]

print(result)

if audio is not None:
    print(audio)
if video is not None:
    print(video)
