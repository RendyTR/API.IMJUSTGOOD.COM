from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.kbbi("komputer")

print(data["result"]["desc"])