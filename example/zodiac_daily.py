from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.zodiac("aries")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "\nSign : {}".format(data["result"]["zodiac"])
result  +=  "\nCouple : {}".format(data["result"]["couple"])
result  +=  "\nDate Range : {}".format(data["result"]["date"])
result  +=  "\nLucky Color : {}".format(data["result"]["color"])
result  +=  "\nLucky Time : {}".format(data["result"]["time"])
result  +=  "\nLucky Number : {}".format(data["result"]["number"])
result  +=  "\nProfile : {}\n".format(data["result"]["profile"])
result  +=  "\nPublic : {}\n".format(data["result"]["public"])
result  +=  "\nMoney : {}\n".format(data["result"]["money"])
result  +=  "\nCareer : {}\n".format(data["result"]["career"])
result  +=  "\nLove Couple : {}\n".format(data["result"]["love"]["couple"])
result  +=  "\nLove Single : {}\n".format(data["result"]["love"]["single"])
result  +=  "\nImage URL : {}".format(data["result"]["image"])

print(result)
