from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.bmkg()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "INFO GEMPA BMKG"
result  +=  "\nTanggal : {}".format(data["result"]["tanggal"])
result  +=  "\nPukul : {}".format(data["result"]["pukul"])
result  +=  "\nLokasi : {}".format(data["result"]["lokasi"])
result  +=  "\nWilayah : {}".format(data["result"]["wilayah"])
result  +=  "\nKordinat : {}".format(data["result"]["kordinat"])
result  +=  "\nKedalaman : {}".format(data["result"]["kedalaman"])
result  +=  "\nKekuatan : {}".format(data["result"]["kekuatan"])
result  +=  "\nArahan : {}".format(data["result"]["arahan"])
result  +=  "\nSaran : {}".format(data["result"]["saran"])
result  +=  "\nSkema Gambar URL : {}".format(data["result"]["skema"])

print(result)