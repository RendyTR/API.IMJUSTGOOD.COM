from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.topnews()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "DAILY TOP NEWS"

for i in range(len(data["result"])):

    result  +=  "\n{}. {}".format((i+1), data["result"][i]["title"])
    result  +=  "\nSource : {}".format(data["result"][i]["source"])
    result  +=  "\nAuthor : {}".format(data["result"][i]["author"])
    result  +=  "\nPage URL : {}".format(data["result"][i]["url"])

print(result)