from justgood import imjustgood

api      =  imjustgood("YOUR_APIKEY_HERE")
data     =  api.resi("jne", "CGK2H03789568816")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   = "{}\n".format(data["result"]["courier"])
result  +=  "\nResi : {}".format(data["result"]["code"])
result  +=  "\nStatus : {}".format(data["result"]["status"])
result  +=  "\nJenis : {}".format(data["result"]["service"])
result  +=  "\nBerat : {}".format(data["result"]["weight"])
result  +=  "\nHarga : {}".format(data["result"]["price"])
result  +=  "\nPukul : {}".format(data["result"]["time"])
result  +=  "\nTanggal : {}\n".format(data["result"]["date"])
result  +=  "\nDeskripsi : {}\n".format(data["result"]["desc"])
result  +=  "\nPengirim : {}, {}\n".format(data["result"]["sender"]["name"],data["result"]["sender"]["city"])
result  +=  "\nPenerima : {}, {}\n".format(data["result"]["receiver"]["name"],data["result"]["receiver"]["city"])

if data["result"]["timeExpress"] != []:

    for a in data["result"]["timeExpress"]:

        result += "\n[ {} ]".format(a["date"])
        result += "\nDeskripsi : {}".format(a["desc"])
        result += "\nLokasi : {}\n".format(a["location"])

print(result)
