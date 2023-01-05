from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.calc("10+10x10:10-10")

print(data["result"])