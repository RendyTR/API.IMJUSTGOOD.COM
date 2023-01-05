from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.B64Encode("Imjustgood Developer API")

print(data["result"])