from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.corona()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   = "CORONA VIRUS QUICKCOUNT\n"

result  +=  "\n{}\n".format(data["result"]["date"])

result  +=  "\nWorld Data"

result  +=  "\n   Case : {}".format(data["result"]["world"]["case"])
result  +=  "\n   Fit : {}".format(data["result"]["world"]["fit"])
result  +=  "\n   Rip : {}\n".format(data["result"]["world"]["rip"])

result  +=  "\nIndonesia Data"

result  +=  "\n   Case : {}".format(data["result"]["indonesia"]["case"])
result  +=  "\n   Fit : {}".format(data["result"]["indonesia"]["fit"])
result  +=  "\n   Rip : {}".format(data["result"]["indonesia"]["rip"])

print(result)