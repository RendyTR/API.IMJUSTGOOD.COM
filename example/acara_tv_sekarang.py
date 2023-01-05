from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.acaratv()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "ACARA TV HARINI"

for a in data["result"]:

    for b in a:

        result  +=  "\nChannel : {}\n".format(b)

        for c in a[b]:

            result  +=  "{}\n".format(c)

print(result)
