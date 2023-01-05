from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.vagina()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   = "Vagina : {}".format(data["result"]["vagina"])
result  +=  "\nDepth : {}".format(data["result"]["depth"])
result  +=  "\nGrip : {}".format(data["result"]["grip"])
result  +=  "\nHumidity : {}".format(data["result"]["humidity"])
result  +=  "\nElasticity : {}".format(data["result"]["elasticity"])
result  +=  "\nDescription : {}".format(data["result"]["description"])
result  +=  "\nPicture URL : {}".format(data["result"]["picture"])

print(result)
