from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.gif("computer")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "GIF SEARCH RESULT :"

for i in range(len(data["result"])):

    result  +=  "\n{}. {}".format((i+1), data["result"][i])

print(result)
