from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")

# GET STAMPLIST NUMBER
# https://api.imjustgood.com/stamplist

data    =  api.stamplist()

result  =  "STAMPLIST :"

for x in data:

    result += "\n{} ({})".format(data[x], x)

print(result)

# EXAMPLE GET CERTAIN ATTRIBUTES

number  = "34"
image   = "https://i.ibb.co/vPJg8HG/example.jpg"
data    = api.stamp(number,image)

result  = "STAMP : {}".format(data["result"]["stamp"])
result += "IMAGE URL : {}".format(data["result"]["image"])

print(result)
