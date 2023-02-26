from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.photohack("Image/example.jpg", "YOUR_TEXT_HERE", effect="liputan6")

print(data["result"])