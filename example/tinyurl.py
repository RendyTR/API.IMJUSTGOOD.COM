from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.tinyurl("https://www.google.com")

print(data["result"])