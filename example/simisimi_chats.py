from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.simisimi("kenapa anda jomnlo ?")

print(data["result"])