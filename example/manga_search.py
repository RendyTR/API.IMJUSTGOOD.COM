from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.mangaSearch("boruto")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "{}".format(data["result"]["title"])
result  +=  "\nAuthor : {}".format(data["result"]["author"])
result  +=  "\nGenre : {}".format(data["result"]["genre"])
result  +=  "\nRating : {}".format(data["result"]["rating"])
result  +=  "\nRelease : {}".format(data["result"]["release"])
result  +=  "\nStatus : {}".format(data["result"]["status"])
result  +=  "\nType : {}".format(data["result"]["type"])
result  +=  "\nUpdate : {}\n".format(data["result"]["updated"])
result  +=  "\nSynopsis : {}\n".format(data["result"]["synopsis"])
result  +=  "\nThumbnail URL: {}".format(data["result"]["thumbnail"])

print(result)
