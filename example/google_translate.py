from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.translate("id", "hasta la vista baby")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   = "From Language : {} ".format(data["result"]["fromLanguage"])
result  += "To Language : {}".format(data["result"]["toLanguage"])
result  += "Traslation : {}".format(data["result"]["translate"])

print(result)

# GET LANGUAGE CODE HERE
# https://api.imjustgood.com/language/code
