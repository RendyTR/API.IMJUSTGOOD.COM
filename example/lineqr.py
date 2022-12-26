from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.lineqr(
    appName="DESKTOPMAC\t7.13.2\tMac\t12.0",
    sysName="IMJUSTGOOD",
    cert=None
)
cbpin   = data["result"]["callback"]["pin"]
cbtoken = data["result"]["callback"]["token"]
qrlink  = data["result"]["qr"]
barcode = data["result"]["barcode"]
print(qrlink)
print(barcode)

data    = api.lineqrGetPin(cbpin)
if data["status"] == 200:
    pin = data["result"]["pin"]
    print(pin)

data    = api.lineqrGetToken(cbtoken)
apps    = data["result"]["app"]
cert    = data["result"]["cert"]
token   = data["result"]["token"]
result  = "Application : {}\n\n".format(apps)
result += "Certified : {}\n\n".format(cert)
result += "Authtoken : {}\n\n".format(token)
print(result)
