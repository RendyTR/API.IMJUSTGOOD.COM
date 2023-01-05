from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.search("imjustgood api")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "GOOGLE SEARCH RESULT :"

for i in range(len(data["result"])):

    main     =  data["result"][i]
 
    result  +=  "\n{}. {}".format((i+1), main["title"])
    result  +=  "\n{}".format(main["snippet"])
    result  +=  "\n{}".format(main["url"])

print(result)
