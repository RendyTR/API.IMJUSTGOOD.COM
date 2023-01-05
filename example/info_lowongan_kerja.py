from justgood import imjustgood

api          =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data         =  api.karir()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result       =  "INFO LOWONGAN KERJA :\n"

for i in range(len(data["result"])):

    main     =  data["resul"][i]

    result  +=  "\n{}. {}".format((i+1), main["perusahaan"])
    result  +=  "\nLokasi : {}".format(main["lokasi"])
    result  +=  "\nProfesi : {}".format(main["profesi"])
    result  +=  "\nBagian : {}".format(main["bagian"])
    result  +=  "\nJabatan : {}".format(main["jabatan"])
    result  +=  "\nGaji : {}".format(main["gaji"])
    result  +=  "\nPendidikan : {}".format(main["pendidikan"])
    result  +=  "\nPenngalaman : {}".format(main["penngalman"])
    result  +=  "\nSyarat : {}".format(main["syarat"])
    result  +=  "\nDeskirpsi : {}".format(main["deskripsi"])
    result  +=  "\nSumber : {}\n".format(main["sumber"])

print(result)
