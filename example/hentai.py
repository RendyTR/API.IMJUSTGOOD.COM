from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.hentai()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "HENTAI RESULT :"

for i in range(len(data["result"])):

    result += "\n{}. {}".format((i+1), data["result"][i])

print(result)
