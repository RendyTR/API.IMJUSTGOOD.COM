from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.instagram("the.autobots_corp")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "ID : {}".format(data["result"]["id"])
result  +=  "\nUsername : {}".format(data["result"]["username"])
result  +=  "\nFullname : {}".format(data["result"]["fullname"])
result  +=  "\nBiography : {}".format(data["result"]["biography"])
result  +=  "\nWebsite : {}".format(data["result"]["website"])
result  +=  "\nPrivate : {}".format(data["result"]["private"])
result  +=  "\nVerified : {}".format(data["result"]["verified"])
result  +=  "\nBusiness : {}".format(data["result"]["business"]["status"])
result  +=  "\nCategory : {}".format(data["result"]["business"]["category"])
result  +=  "\nFollower : {}".format(data["result"]["follower"])
result  +=  "\nFollowing : {}".format(data["result"]["following"])
result  +=  "\nPost : {}".format(data["result"]["post"])

if data["result"]["highlights"] != []:

    main     =  data["result"]["highlights"]
    result  +=  "\n\nHighlights :"

    for i in range(len(main)):

        result  +=  "\n{}. {} ({})".format((i+1), main[i]["title"], main[i]["count"])
        result  +=  "\nPage URL : {}".format(main[i]["url"])
        result  +=  "\nThumnail URL : {}\n".format(main[i]["cover"])
 
if data["result"]["lastpost"] != []:

    main     =  data["result"]["lastpost"]
    result  +=  "\n\nLastpost :"

    for i in range(len(main)):
        
        result  +=  "\n{}. {}".format((i+1), main[i]["caption"])
        result  +=  "\n{}".format(main[i]["url"])
        result  +=  "\n   Like : {}".format(main[i]["like"])
        result  +=  "\n   Comment : {}".format(main[i]["comment"])
        result  +=  "\n   Created : {}".format(main[i]["created"])
        result  +=  "\n   PageUrl : {}\n".format(main[i]["page"])

result  +=  "\nPicture URL : {}".format(data["result"]["picture"])
result  +=  "\nProfile url : {}".format(data["result"]["profile"])

print(result)