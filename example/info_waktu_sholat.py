from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.adzan("palembang")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "Info Waktu Sholat"
result  +=  "\nWilayah : {}".format(data["result"]["wilayah"])
result  +=  "\nTanggal : {}\n".format(data["result"]["tanggal"])
result  +=  "\nImsyak : {}".format(data["result"]["adzan"]["imsyak"])
result  +=  "\nSubuh : {}".format(data["result"]["adzan"]["subuh"])
result  +=  "\nTerbit : {}".format(data["result"]["adzan"]["terbit"])
result  +=  "\nDhuha : {}".format(data["result"]["adzan"]["dhuha"])
result  +=  "\nDzuhur : {}".format(data["result"]["adzan"]["dzuhur"])
result  +=  "\nAshar : {}".format(data["result"]["adzan"]["ashar"])
result  +=  "\nMaghrib : {}".format(data["result"]["adzan"]["maghrib"])
result  +=  "\nIsya : {}".format(data["result"]["adzan"]["isya"])

print(result)
