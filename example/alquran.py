from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")

# GET LIST AL-QUR'AN ALL SURAH
# https://api.imjustgood.com/alquran=list

data     =  api.alquran()

result   =  "AL-QUR'AN SURAH :"
for qs in data:
    result  +=  "\n{}".format(qs)

print(result)

# EXAMPLE GET CERTAIN AL-QUR'AN SURAH ATTRIBUTES

data     =  api.alquranQS("al-ikhlas")

audio    =  data["result"]["audio"]
number   =  data["result"]["number"]
total    =  data["result"]["verse"]
meaning  =  data["result"]["meaning"]
place    =  data["result"]["place"]
desc     =  data["result"]["desc"]
verse    =  data["result"]["verses"]
arab     =  data["result"]["title"]["ar"]
latin    =  data["result"]["title"]["id"]

result   = "[QS:{}][{}]\n".format(number, total)
result  += "\n{}".format(arab)
result  += "\n{} ({})\n".format(latin, meaning)

for i in range(len(verse)):

    result += "\n{}".format(verse[i]["ar"])
    result += "\n{}. {}\n".format((i+1), verse[i]["id"])

result  += "\nDiturunkan di : {}\n".format(place)
result  += "\n{}\n".format(desc)
result  += "\nAudio URL : {}".format(audio)

print(result)