from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.cctv_code()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "DAFTAR CCTV CAMERA\n"

for a in data["result"]["available"]:

    result  +=  "{} {}\n".format(a, data["result"]["available"][a])

result  +=  "\nCCTV AKTIF SAAT INI\n"

for b in data["result"]["active"]:

    result  +=  "{} {}\n".format(b, data["result"]["active"][b])

print(result)
