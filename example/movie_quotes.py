from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.movie_quotes()

print(data["result"])