from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.customlink("example_label_name", "https://example.com")

print(data["result"])