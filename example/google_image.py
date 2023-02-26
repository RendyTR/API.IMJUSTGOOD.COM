from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.image("robocop")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "GOOGLE IMAGE RESULT :"

for i in range(len(data["result"])):

    result  +=  "\n{}. {}".format((i+1), data["result"][i])

print(result)
