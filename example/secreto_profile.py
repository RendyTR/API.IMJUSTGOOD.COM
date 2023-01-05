from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.secreto("https://secreto.site/a0wpl4")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Author : {}".format(data["result"]["author"])
result  +=  "\nSecretId : {}".format(data["result"]["secretId"])

if data["result"]["timeline"] != []:

    result  +=  "\nTimeline : None"

    for i in range(len(data["result"]["timeline"])):

        main  =  data["result"]["timeline"][i]

        result  +=  "\n{}. {}".format((i+1), main["message"])
        result  +=  "\n{}".format(main["pagelink"])

print(result)