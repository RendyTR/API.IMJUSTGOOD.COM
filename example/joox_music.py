from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.joox("lathi")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

thumb    =  data["result"]["thumbnail"]
audio    =  data["result"]["m4aUrl"]

result   =  "Title : {}\n".format(data["result"]["title"])
result  +=  "Singer : {}\n".format(data["result"]["singer"])
result  +=  "Duration : {}\n".format(data["result"]["duration"])
result  +=  "File size : {}".format(data["result"]["size"])

print(thumb, result, audio)
