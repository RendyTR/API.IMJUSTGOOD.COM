from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.cinema("garut")

print(data)

# EXAMPLE GET CINEMA LIST

result   =  "JADWAL NONTON 21 CINEMA\n\n"
result  +=  "City : {}\n".format(data["result"]["city"])

for i in range(len(data["result"]["data"])):

    result  +=  "\n{}. {}".format((i+1),data["result"]["data"][i]["cinema"])

print(result)

# EXAMPLE GET LIST MOVIE CINEMA

number   =  1

main     =  data["result"]["data"][number_-1]

result   =  "{}".format(main["cinema"])
result  +=  "\n{}\n".format(main["address"])
result  +=  "\nNow playing :\n"

for i in range(len(main["nowPlaying"])):

    result  +=  "{}. {}\n".format((i+1),main["nowPlaying"][i]["movie"])

result  +=  "\nImage URL : {}".format(main["studioImage"])

print(result)

# EXAMPLE GET MOVIE INFORMATION

number_a  =  1
number_b  =  1

main      =  data["result"]["data"][number_a-1]
main      =  main["nowPlaying"][number_b-1]

result    =  "{}".format(main["movie"])
result   += "\n\nPrice : {}".format(main["price"])
result   += "\n\nShowtime :\n"

for x in main["showtime"]:

    result += "-{}\n".format(x)

result   += "\nGenre : {}".format(main["genre"])
result   += "\nDuration : {}".format(main["duration"])
result   += "\nDirector : {}".format(main["director"])
result   += "\nActor : {}".format(main["actor"])
result   += "\nSynopsis : {}".format(main["synopsis"])
result   += "\nPoster URL : {}".format(main["poster"])

print(result)