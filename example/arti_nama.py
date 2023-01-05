from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.nama("undertaker")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Nama : {}".format(data["result"]["name"])
result  +=  "\nKarakter : {}".format(data["result"]["definition"])
result  +=  "\nDeskripsi : {}".format(data["result"]["description"])

print(result)
