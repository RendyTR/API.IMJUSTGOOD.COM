from justgood import imjustgood

text1  =  "top"
text2  =  "bottom"
image  =  "http://www.gstatic.com/webp/gallery/1.png"

api    =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data   =  api.meme(text1, text2, imageUrl)

print(dara["result"])
