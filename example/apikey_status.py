from justgood import imjustgood

api     = imjustgood("INSERT_YOUR_APIKEY_HERE")
data    = api.status()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "ID : {}".format(data["result"]["id"])
result += "\nType : {}".format(data["result"]["type"])
result += "\nUsage : {}".format(data["result"]["usage"])
result += "\nExpired : {}".format(data["result"]["expired"])
result += "\nRestart : {}".format(data["result"]["restart"])
result += "\nTimeleft : {}".format(data["result"]["timeleft"])
print(result)
