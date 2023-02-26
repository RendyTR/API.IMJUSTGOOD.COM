from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.removebg(imagepath="example.jpg", background=None)

print(data["result"])