from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.playstore("termius")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "GOOGLE PLAYSTORE RESULT :"

for i in range(len(data["result"])):

    main     =  data["result"][i]

    result  +=  "\n{}. {}".format((i+1), main["title"])
    result  +=  "\nDeveloper : {}".format(main["developer"])
    result  +=  "\nDescription : {}".format(main["description"])
    result  +=  "\nPage URL : {}".format(a["pageUrl"])
    result  +=  "\nHeader URL : {}".format(main["header"])
    result  +=  "\nThumbnail URL : {}".format(main["thumbnail"])

print(result)