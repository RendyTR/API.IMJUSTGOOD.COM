from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.tiktok("victoriapfeifer")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Username : {}".format(data["result"]["username"])
result  +=  "\nFullname : {}".format(data["result"]["fullname"])
result  +=  "\nPrivate : {}".format(data["result"]["private"])
result  +=  "\nVerified : {}".format(data["result"]["private"])
result  +=  "\nBiography : {}".format(data["result"]["biography"])
result  +=  "\nFollowers : {}".format(data["result"]["followers"])
result  +=  "\nFollowing : {}".format(data["result"]["following"])
result  +=  "\nLikes : {}".format(data["result"]["likes"])
result  +=  "\nVideos : {}".format(data["result"]["videos"])
result  +=  "\nWebsite : {}".format(data["result"]["website"])
result  +=  "\nYoutube : {}".format(data["result"]["social"]["youtube"])
result  +=  "\nTwitter : {}".format(data["result"]["social"]["twitter"])
result  +=  "\nInstagram : {}".format(data["result"]["social"]["instagram"])

if data["result"]["lastpost"] != []:

    main     =  data["result"]["lastpost"]

    result  +=  "\n\nLast Contents :\n"

    for i in range(len(main)):

        result  +=  "{}. {}\n".format((i+1), main[i]["desc"])

result  +=  "\nPicture URL : {}".format(data["result"]["pictureUrl"])
result  +=  "\nProfile URL : {}".format(data["result"]["profileUrl"])

print(result)

# EXAMPLE GET LAST CONTENTS ATTRIBUTES

number   =  1
result   =  "Not found"

if data["result"]["lastpost"] != []:

    main     =  data["result"]["lastpost"][number-1]

    result   =  "Caption : {}".format(main["desc"])
    result  +=  "\nCreated : {}".format(main["created"])
    result  +=  "\nLike : {}".format(main["like"])
    result  +=  "\nShare : {}".format(main["share"])
    result  +=  "\nComment : {}".format(main["comment"])
    result  +=  "\nPlaying : {}".format(main["playing"])
    result  +=  "\nDownload : {}".format(main["download"])
    result  +=  "\nThumbnail URL: {}".format(main["poster"])
    result  +=  "\nVideo URL : {}".format(main["videoUrl"])
    result  +=  "\nPage URL: {}".format(a["pageUrl"])

print(result)