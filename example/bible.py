from justgood import imjustgood

api        =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data       =  api.bible()

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

indonesia  = data["result"]["indonesia"] 
english    = data["result"]["english"]

result     = "RANDOM BIBLE"
result    += "\n\n[EN][VER:{}][{}] {}".format(english["version"],english["reference"],english["text"])
result    += "\n\n[ID][VER:{}][{}] {}".format(indonesia["version"],indonesia["reference"],indonesia["text"])

print(result)