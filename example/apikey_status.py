from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.status()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "ID : {}\n".format(data["result"]["id"])
result  +=  "Type : {}\n".format(data["result"]["type"])
result  +=  "Usage : {}\n".format(data["result"]["usage"])
result  +=  "Expired : {}\n".format(data["result"]["expired"])
result  +=  "Restart : {}\n".format(data["result"]["restart"])
result  +=  "Timeleft : {}".format(data["result"]["timeleft"])

print(result)
