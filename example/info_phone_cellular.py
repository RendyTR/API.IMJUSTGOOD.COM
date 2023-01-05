from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.cellular("iphone 14")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  " PHONE CELLULAR RESULT :\n"

for i in range(len(data["result"])):

    main     =  data["result"][i]

    result += "\n{}. {}".format((i+1), main["brands"])
    result += "\nRelease : {}".format(main["release"])
    result += "\nChipset : {}".format(main["chipset"])
    result += "\nScreen : {}".format(main["screen"])
    result += "\nBattery : {}".format(main["battery"])
    result += "\nDisplay : {}".format(main["display"])
    result += "\nRam : {}".format(main["ram"])
    result += "\nStorage : {}".format(main["storage"])
    result += "\nThumbnail URL : {}".format(main["thumbnail"])
    result += "\nPage URL : {}\n".format(main["pageUrl"])

print(result)