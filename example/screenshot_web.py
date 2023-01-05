from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.screenshot("www.google.com")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "SCREENSHOT RESULT"
result  +=  "\nDesktop Version : {}".format(data["result"]["desktop"])
result  +=  "\nMobile Version : {}".format(data["result"]["mobile"])

print(result)
