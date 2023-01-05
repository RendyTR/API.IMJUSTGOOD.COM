from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.B64Decode("SW1qdXN0Z29vZCBEZXZlbG9wZXIgQVBJ")

print(data["result"])