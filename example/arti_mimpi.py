from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.mimpi("ciuman")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "ARTI MIMPI\n"

for a in data["result"]:

    result += "\nMimpi : {}".format(a["dream"])
    result += "\nArti : {}\n".format(a["meaning"])

print(result)