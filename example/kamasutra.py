from justgood import imjustgood

api     = imjustgood("INSERT_YOUR_APIKEY_HERE")
data    = api.kamasutra()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   = "Style : {}".format(data["result"]["style"])
result  += "\nDescription : {}".format(data["result"]["description"])
result  += "\nPicture URL: {}".format(data["result"]["thumbnail"])

print(result)
