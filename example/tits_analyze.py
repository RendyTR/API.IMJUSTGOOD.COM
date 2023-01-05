from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.tits()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Tits : {}".format(data["result"]["tits"])
result  +=  "\nSize : {}{}".format(data["result"]["size"],data["result"]["cup"])
result  +=  "\nNipple : {}".format(data["result"]["nipple"])
result  +=  "\nAerola : {}".format(data["result"]["aerola"])
result  +=  "\nDescription : {}".format(data["result"]["description"])
result  +=  "\nPicture URL : {}".format(data["result"]["picture"])

print(result)
