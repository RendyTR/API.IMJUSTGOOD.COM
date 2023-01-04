from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.smuledl("https://www.smule.com/p/1998769355_3429377039")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

thumb    =  None
video    =  None
audio    =  data["result"]["mp3Url"]

result   =  "Username : {}\n".format(data["result"]["username"])
result  +=  "Verified : {}\n".format(data["result"]["verified"])
result  +=  "VIP : {}\n\n".format(data["result"]["vip"])
result  +=  "Title : {}\n".format(data["result"]["title"])
result  +=  "Artist : {}\n".format(data["result"]["artist"])
result  +=  "Type : {}\n".format(data["result"]["type"])
result  +=  "Listens : {}\n".format(data["result"]["listens"])
result  +=  "Loves : {}\n".format(data["result"]["loves"])
result  +=  "Gifts : {}\n".format(data["result"]["gifts"])
result  +=  "Comments : {}\n\n".format(data["result"]["comments"])
result  +=  "{}\n\n{}".format(data["result"]["caption"], data["result"]["creaated"])

if data["result"]["type"] == "video":
    thumb = data["result"]["thumbnail"]
    video = data["result"]["mp4Url"]

print(thumb, result, audio, video)
