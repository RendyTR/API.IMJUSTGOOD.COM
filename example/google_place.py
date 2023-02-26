from justgood import imjustgood

api    =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data   =  api.place("hotel di jakarta", region="id", lang="id")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result = "GOOGLE PLACE\n"
for i in range(len(data["result"])):

    main     =  data["result"][i]

    result  +=  "\n{}. {}".format((i+1), main["name"])
    result  +=  "\nType : {}".format(main["type"])
    result  +=  "\nAddress : {}".format(main["address"])
    result  +=  "\nPhone : {}".format(main["phone"])
    result  +=  "\nLatitude : {}".format(main["latitude"])
    result  +=  "\nLongitude : {}".format(main["longitude"])
    result  +=  "\nReview : {}".format(main["review"])
    result  +=  "\nRating : {}".format(main["rating"])
    result  +=  "\nTimezone : {}".format(main["timezone"])
    result  +=  "\nWebsite : {}".format(main["website"])
    result  +=  "\nMaps URL : {}".format(main["maps"])
    result  +=  "\nImage URL : {}\n".format(main["image"])

print(result)