from justgood import imjustgood

api     =  imjustgood("INSER_YOUR_APIKEY_HERE")
data    =  api.lineapp()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "LINE APP VERSION"

for a in data["result"]:

    result  +=  "\n{} : {}".format(a, data["result"][a])

print(result)
