from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
effect  =  "scifi"
text1   =  "IMJUSTGOOD"
data    =  api.textpro(text1, text2=None, text3=None, effect=effect)

print(data["result"])

# GET MORE EFFECT HERE
# https://api.imjustgood.com/textpro?effect=get
