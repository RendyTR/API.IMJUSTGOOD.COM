from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.imagetext("Do you miss me ?")

print(data["result"])