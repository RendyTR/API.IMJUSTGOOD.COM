from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.tiktokdl("https://vt.tiktok.com/ZS86s89cu/")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Username : {}".format(data["result"]["username"])
result  +=  "\nFullname : {}".format(data["result"]["fullname"])
result  +=  "\nCaption : {}".format(data["result"]["caption"])
result  +=  "\nLike : {}".format(data["result"]["like"])
result  +=  "\nShare : {}".format(data["result"]["share"])
result  +=  "\nComment : {}".format(data["result"]["comment"])
result  +=  "\nDuration : {}".format(data["result"]["duration"])
result  +=  "\nPlaying : {}".format(data["result"]["play"])
result  +=  "\nDownload : {}".format(data["result"]["download"])
result  +=  "\nCreated : {}".format(data["result"]["created"])
result  +=  "\nMusic : {}".format(data["result"]["music"])
result  +=  "\nPicture URL : {}".format(data["result"]["picture"])
result  +=  "\nThumbnail URL : {}".format(data["result"]["thumbnail"])
result  +=  "\nCovertrack URL : {}".format(data["result"]["covertrack"])
result  +=  "\nAudio URL : {}".format(data["result"]["sound"])
result  +=  "\nVideo Watermark URL : {}".format(data["result"]["watermark"])
result  +=  "\nVideo Nowatermark URL : {}".format(data["result"]["no_watermark"])

if data["result"]["images"] != []:

    result  +=  "\nImage URL :"

    for i in range(len(data["result"]["images"])):

        result  +=  "\n{}. {}".format((i+1), data["result"]["images"][i])

print(result)