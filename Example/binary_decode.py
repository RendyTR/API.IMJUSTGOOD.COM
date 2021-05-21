import json, requests

digit_code = "01001001011011010110101001110101011100110111010001100111011011110110111101100100" # example digit code
headers = {"user-agent": "Justgood/5.0"}
host = "https://api.imjustgood.com/binary/digit="+digit_code
data = json.loads(requests.get(host,headers=headers).text)
result = data["result"]
print(result)
