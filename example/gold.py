from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.gold()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "Gold Currency Update\n"
result +=  "\n{}\n".format(data["result"]["update"])
result +=  "\nUSD {}".format(data["result"]["usd"])
result +=  "\nIDR {}".format(data["result"]["idr"])
result +=  "\nKURS {}".format(data["result"]["kurs"])

print(result)
