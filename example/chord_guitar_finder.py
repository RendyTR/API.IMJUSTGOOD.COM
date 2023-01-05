from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.chord("stay")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "{}\n".format(data["result"]["title"])
result  +=  "\n{}".format(data["result"]["chord"])

print(result)