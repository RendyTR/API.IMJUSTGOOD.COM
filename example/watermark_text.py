from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.watermark_text("https://example.com/image.jpg", "IMJUSTGOOD")

print(data["result"])