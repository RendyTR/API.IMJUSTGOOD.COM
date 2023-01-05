from justgood import imjustgood
import random

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.pornstar()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

main     =  random.choice(data["result"])

result   =  "Name : {}".format(main["pornstar"])
result  +=  "\nBirth : {}".format(main["birth"])
result  +=  "\nGender : {}".format(main["gender"])
result  +=  "\nCountry : {}".format(main["country"])
result  +=  "\nHeight : {}".format(main["height"])

if main["gender"] == "male":

    result  +=  "\nDick : {}".format(main["dick"])

if main["gender"] == "female":

    result  +=  "\nBreast : {}".format(main["breast"])
    result  +=  "\nTits : {}".format(main["tits"])

result  +=  "\n\nImage URL : {}".format(main["image"])

print(result)