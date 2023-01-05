from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.urban("wtf")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "URBAN DICTIONARY"
result  +=  "\nDefinition : {}".format(data["result"]["definition"])
result  +=  "\nExample : {}".format(data["result"]["example"])

print(result)
