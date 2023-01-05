from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.jadian("01-01-2023")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Date : {}".format(data["result"]["date"])
result  +=  "\n\nRelated : {}".format(data["result"]["related"])
result  +=  "\n\nDescription : {}".format(data["result"]["description"])

print(result)
