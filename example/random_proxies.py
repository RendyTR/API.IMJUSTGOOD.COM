from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.proxies()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "PROXIES RESULT :\n"

for x in data["result"]:

    result  +=  "\nIP : {}".format(x["ip"])
    result  +=  "\nPort : {}".format(x["port"])
    result  +=  "\nRegion : {}".format(x["region"])
    result  +=  "\nCountry : {}\n".format(x["country"])

print(result)