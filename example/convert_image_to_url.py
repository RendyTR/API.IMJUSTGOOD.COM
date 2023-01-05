from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.imgurl("Image/example.jpg")

print(data["result"])