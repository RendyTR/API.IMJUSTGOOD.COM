from justgood import imjustgood

api      =  imjustgood("INSER_YOUR_APIKEY_HERE")
data     =  api.tiktok("sandrinaazzhra")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

pict     =  data["result"]["pictureUrl"]

result   =  "Username : {}\n".format(data["result"]["username"])
result  +=  "Fullname : {}\n".format(data["result"]["fullname"])
result  +=  "Private : {}\n".format(data["result"]["private"])
result  +=  "Verified : {}\n".format(data["result"]["private"])
result  +=  "Biography : {}\n".format(data["result"]["biography"])
result  +=  "Followers : {}\n".format(data["result"]["followers"])
result  +=  "Following : {}\n".format(data["result"]["following"])
result  +=  "Likes : {}\n".format(data["result"]["likes"])
result  +=  "Videos : {}\n".format(data["result"]["videos"])
result  +=  "Website : {}\n".format(data["result"]["website"])
result  +=  "Youtube : {}\n".format(data["result"]["social"]["youtube"])
result  +=  "Twitter : {}\n".format(data["result"]["website"]["twitter"])
result  +=  "Instagram : {}\n".format(data["result"]["website"]["instagram"])
result  +=  "Picture URL : {}\n".format(data["result"]["pictureUrl"])
result  +=  "Profile URL : {}".format(data["result"]["profileUrl"])

if data["result"]["lastpost"] != []:
    for a in data["result"]["lastpost"]:
        result += "\nLastpost :"
        result += "\n- Caption : {}".format(a["desc"])
        result += "\n- Created : {}".format(a["created"])
        result += "\n- Comments : {}".format(a["comment"])
        result += "\n- Donwload : {}".format(a["download"])
        result += "\n- Playing : {}".format(a["playing"])
        result += "\n- Share : {}".format(a["share"])
        result += "\n- Thumbnail : {}".format(a["poster"])
        result += "\n- Video URL : {}".format(a["videoUrl"])
        result += "\n- Page URL : {}".format(a["pageUrl"])

print(result)
