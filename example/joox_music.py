from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.joox("lathi")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Title : {}\n".format(data["result"]["title"])
result  +=  "Singer : {}\n".format(data["result"]["singer"])
result  +=  "Album : {}\n".format(data["result"]["album"])
result  +=  "Duration : {}\n".format(data["result"]["duration"])
result  +=  "File size : {}\n".format(data["result"]["size"])
result  +=  "M4a URL : {}\n".format(data["result"]["m4aUrl"])
result  +=  "Mp3 URL : {}\n".format(data["result"]["mp3Url"])
result  +=  "Thumbnail URL : {}".format(data["result"]["thumbnail"])

print(result)
