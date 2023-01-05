from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.check_ip("8.8.8.8")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "IP : {}\n".format(data["result"]["query"])
result  +=  "\nCity : {} ({})".format(data["result"]["city"])
result  +=  "\nCountry : {} ({})".format(data["result"]["country"], data["result"]["countryCode"])
result  +=  "\nRegion : {} ({})\n".format(data["result"]["region"], data["result"]["regionName"])
result  +=  "\nLAT : {} ({})".format(data["result"]["lat"])
result  +=  "\nLON : {} ({})".format(data["result"]["lon"])
result  +=  "\nZIP : {} ({})".format(data["result"]["zip"])
result  +=  "\nORG : {} ({})".format(data["result"]["org"])
result  +=  "\nAS : {} ({})".format(data["result"]["as"])
result  +=  "\nISP : {} ({})\n".format(data["result"]["isp"])
result  +=  "\nTimezone : {} ({})".format(data["result"]["timezone"])

print(result)