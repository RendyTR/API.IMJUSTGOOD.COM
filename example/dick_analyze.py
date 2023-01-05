from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.dick()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Dick : {}".format(data["result"]["dick"])
result  +=  "\nSize : {}".format(data["result"]["size"])
result  +=  "\nAbility : {}".format(data["result"]["ability"])
result  +=  "\nFlexibility : {}".format(data["result"]["flexibility"])
result  +=  "\nDescription : {}".format(data["result"]["description"])
result  +=  "\nPicture URL : {}".format(data["result"]["picture"])

print(result)
