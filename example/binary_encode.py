from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.BinaryEncode("hahaha")

print(data["result"])