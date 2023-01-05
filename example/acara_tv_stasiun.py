from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.acaratv_channel("globaltv")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "JADWAL ACARA TV"

for a in data["result"]:

    result  +=  "\n{}".format(a)

print(result)