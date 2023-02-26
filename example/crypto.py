from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.crypto("IDR")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "Crypto Currency Update\n"

for i in range(len(data["result"])):

    main     =  data["result"][i]

    result  +=  "\n{}. {} ({})".format((i+1), main["name"], main["symbol"])
    result  +=  "\nPrice : {}".format(main["price"])
    result  +=  "\nUpdate : {}\n".format(main["update"])

print(result)
