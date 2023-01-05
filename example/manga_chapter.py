from justgood import imjustgood

api     =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data    =  api.mangaChapter("boruto-naruto-next-generations-chapter-67-1")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result  =  "{}".format(data["result"]["title"])

for i in range(len(data["result"]["manga"])):

    result  +=  "\n{}. {}".format((i+1), data["result"]["manga"][i])

print(result)
