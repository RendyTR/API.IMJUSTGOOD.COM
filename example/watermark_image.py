from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.watermark_image("https://example.com/image.jpg", "https://example.com/icon.png")

print(data["result"])

# WATERMARK IMAGE ONLY SUPPORT PNG FILE TYPE