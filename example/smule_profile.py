from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.smule("avamax")
print(data)

# EXAMPLE GET PROFILE ATTRIBUTES

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
result  +=  "Picture URL : {}\n".format(data["result"]["pictureUrl"])
result  +=  "Profile URL : {}".format(data["result"]["profileUrl"])

if data["result"]["post"] != []:
    result += "\n\nPerformances :"
    for i in range(len(data["result"]["post"])):
        title   = data["result"]["post"][i]["title"]
        result += "\n   {}. {}".format(number+1, title)

print(result)

# EXAMPLE GET PERFORMANCES ATTRIBUTES

select_num    =  1
result        =  "Not found"
performances  =  data["result"]["post"]

if performances != []:

    main      =  performances[select_num-1]
    data      =  api.smuledl(main["pageUrl"])

    result    =  "Artist : {}\n".format(data["artist"])
    result   +=  "Title : {}\n".format(data["title"])
    result   +=  "Caption : {}\n".format(data["caption"])
    result   +=  "Created : {}\n".format(data["created"])
    result   +=  "Love : {}\n".format(data["loves"])
    result   +=  "Gift : {}\n".format(data["gifts"])
    result   +=  "Listen : {}\n".format(data["listens"])
    result   +=  "Comment : {}\n".format(data["comments"])
    result   +=  "Audio URL : {}".format(data["mp3Url"])

    if data["result"]["type"] == "video":
        result +=  "\nVideo URL : {}".format(data["result"]["mp4Url"])
    result     +=  "\nThumbnail URL : {}".format(data["thumbnail"])

print(result)
