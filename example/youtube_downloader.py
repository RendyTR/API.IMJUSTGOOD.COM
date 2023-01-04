from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.youtubedl("https://youtu.be/POG1xVW-1jQ")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

thumb    =  data["result"]["thumbnail"]
video    =  data["result"]["audioUrl"]
audio    =  data["result"]["videourl"]

result   =  "Title : {}\n".format(data["result"]["title"])
result  +=  "Author : {}\n".format(data["result"]["author"])
result  +=  "Duration : {}\n".format(data["result"]["duration"])
result  +=  "Watched : {}\n\n".format(data["result"]["watched"])
result  +=  "Description :\n{}\n\n".format(data["result"]["description"])
result  +=  "Page URL : {}".format(data["result"]["pageUrl"])

print(thumb, result, audio, video)
