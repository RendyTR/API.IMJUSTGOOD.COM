from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.cuaca("surabaya")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "{}".format(data["result"]["location"])
result += "\nCuaca : {}".format(data["result"]["description"])
result += "\nSuhu : {}".format(data["result"]["temperature"])
result += "\nAngin : {}".format(data["result"]["wind"])
result += "\nKelembapan : {}".format(data["result"]["humidity"])
print(result)