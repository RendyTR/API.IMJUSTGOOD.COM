from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.lahir("17-08-1945")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Lahir : {}".format(data["result"]["lahir"])
result  +=  "\nHari : {}".format(data["result"]["hari"])
result  +=  "\nZodiac : {}".format(data["result"]["zodiak"])
result  +=  "\nUltah : {}".format(data["result"]["ultah"])
result  +=  "\nUsia : {}".format(data["result"]["usia"])

print(result)
