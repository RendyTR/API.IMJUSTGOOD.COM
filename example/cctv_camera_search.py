from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.cctvSearch("119")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "CCTV CAMERA INFO"
result  +=  "\nArea : {}".format(data["result"]["area"])
result  +=  "\nWilayah : {}\n".format(data["result"]["wilayah"])
result  +=  "\n{}\n".format(data["result"]["camera"])
result  +=  "\nVideo URL: {}".format(data["result"]["video"])
result  +=  "\nThumbnail URL: {}".format(data["result"]["thumbnail"])

print(result)
