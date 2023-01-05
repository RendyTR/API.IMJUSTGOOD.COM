from justgood import imjustgood

api      =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data     =  api.github("rendytr")

print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES

result   =  "ID : {}".format(data["result"]["id"])
result  +=  "\nType : {}".format(data["result"]["type"])
result  +=  "\nUsername : {}".format(data["result"]["username"])
result  +=  "\nFullname : {}".format(data["result"]["fullname"])
result  +=  "\nBiography : {}".format(data["result"]["bio"])
result  +=  "\nBlog : {}".format(data["result"]["blog"])
result  +=  "\nEmail : {}".format(data["result"]["email"])
result  +=  "\nCompany : {}".format(data["result"]["company"])
result  +=  "\nCreated : {}".format(data["result"]["created_at"])
result  +=  "\nUpdated : {}".format(data["result"]["updated_at"])
result  +=  "\nLocation : {}".format(data["result"]["location"])
result  +=  "\nRepositories : {}".format(data["result"]["repositories"])
result  +=  "\nFollower : {}".format(data["result"]["follower"])
result  +=  "\nFollowing : {}".format(data["result"]["following"])
result  +=  "\nAvatar URL: {}".format(data["result"]["avatar"])
result  +=  "\nProfile URL: {}".format(data["result"]["page"])

print(result)