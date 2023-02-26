from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.bible()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "{}".format(data["result"]["reference"])
result  +=  "\n\n{}".format(data["result"]["english"])
result  +=  "\n\n{}".format(data["result"]["indonesia"])

print(result)
