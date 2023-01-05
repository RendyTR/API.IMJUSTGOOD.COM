from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.lineqr(
    appName="DESKTOPWIN\t7.13.2\tWindows\t10.0",
    sysName="IMJUSTGOOD",
    cert=None
)

ipaddress  =  data["result"]["ip"]
linkqr     =  data["result"]["qr"]
barcode    =  data["result"]["barcode"]
callback   =  data["result"]["callback"]
print("LINK QR : " + qrlink)
print("IMAGE BARCODE : " + barcode)

data  =  api.lineqrGetPin(callback["pin"])
if data["status"] == 200:
    pincode = data["result"]["pin"]
    print("PIN CODE : " + pincode)

data   =  api.lineqrGetToken(callback["token"])
app    =  data["result"]["app"]
cert   =  data["result"]["cert"]
token  =  data["result"]["token"]
print("APP : " + app)
print("IP : " + ipaddress)
print("CERTIFIED : " + cert)
print("AUTHTOKEN : " + token)