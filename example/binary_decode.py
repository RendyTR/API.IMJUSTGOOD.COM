from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.BinaryDecode("01001001011011010110101001110101011100110111010001100111011011110110111101100100")

print(data["result"])