import json, requests, threading

class imjustgood(threading.Thread):
    def __init__(self, apikey):
        super(imjustgood, self).__init__()
        self.host    = "https://api.imjustgood.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/51.0.2704.106",
            "Apikey": apikey
        }
        self.apikey  = apikey
        self.session = requests.Session()

    def GoodJson(self, data):
        return str(json.dumps(data, indent=4, sort_keys=True))

    def Get(self, path, headers=None, params=None):
        if headers is None:
            headers = self.headers
        else:
            headers = {**headers, **self.headers}
        response = self.session.get(self.host+path, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception("ERROR API SYSTEM")
        result = json.loads(response.text)
        if result["status"] != 200:
           raise Exception(result["message"])
        return result

    def Post(self, path, headers=None, data=None, files=None, isjson=None):
        if headers is None:
            headers = self.headers
        else:
            headers = {**headers, **self.headers}
        response = self.session.post(self.host+path, headers=headers, data=data, files=files, json=isjson)
        if response.status_code != 200:
            raise Exception("ERROR API SYSTEM")
        result = json.loads(response.text)
        if result["status"] != 200:
           raise Exception(result["message"])
        return result

    def status(self):
        params = {"apikey": self.apikey }
        return self.Get("/status", params=params)

    def youtube(self, query):
        return self.Get("/youtube="+query)

    def youtubedl(self, url):
        return self.Get("/youtubedl="+url)

    def joox(self, query):
        return self.Get("/joox="+query)
    
    def lyric(self, query):
        return self.Get("/lyric="+query)

    def chord(self, query):
        return self.Get("/chord="+query)

    def smule(self, username):
        return self.Get("/smule="+username)
    
    def smuledl(self, url):
        return self.Get("/smuledl="+url)

    def tiktok(self, username):
        return self.Get("/tiktok="+username)
    
    def tiktokdl(self, url):
        return self.Get("/tiktokdl="+url)

    def instagram(self, username):
        return self.Get("/instagram="+username)
    
    def instapost(self, url):
        return self.Get("/instapost="+url)

    def instastory(self, username):
        return self.Get("/instastory="+username)

    def twitter(self, username):
        return self.Get("/twitter="+username)

    def twitterdl(self, url):
        params = {"url": url }
        return self.Get("/twitter/video", params=params)

    def snackvideo(self, url):
        params = {"url": url }
        return self.Get("/snackvideo", params=params)

    def secreto(self, url):
        params = {"url": url }
        return self.Get("/secreto", params=params)

    def facebookdl(self, url):
        params = {"url": url }
        return self.Get("/facebook/video", params=params)

    def pinterest(self, url):
        params = {"url": url }
        return self.Get("/pinterest", params=params)

    def github(self, username):
        return self.Get("/github="+username)

    def playstore(self, query):
        return self.Get("/playstore="+query)

    def translate(self, lang, text):
        return self.Get("/translate/"+lang+"="+text)

    def image(self, query):
        return self.Get("/image="+query)

    def wallpaper(self, query):
        return self.Get("/wallpaper="+query)

    def porn(self, query):
        return self.Get("/porn="+query)

    def pornstar(self):
        return self.Get("/pornstar")

    def hentai(self):
        return self.Get("/hentai")

    def kamasutra(self):
        return self.Get("/kamasutra")

    def dick(self):
        return self.Get("/dick")

    def tits(self):
        return self.Get("/tits")

    def vagina(self):
        return self.Get("/vagina")

    def movie(self, query):
        return self.Get("/movie="+query)

    def movie_quotes(self):
        return self.Get("/movie/quotes")

    def cinema(self, cityname):
        return self.Get("/cinema="+cityname)

    def tinyurl(self, url):
        return self.Get("/tinyurl="+url)

    def bitly(self, url):
        return self.Get("/bitly="+url)

    def kbbi(self, query):
        return self.Get("/kbbi="+query)

    def topnews(self):
        return self.Get("/topnews")

    def wikipedia(self, query):
        return self.Get("/wikipedia="+query)

    def urban(self, query):
        return self.Get("/urban="+query)

    def zodiac(self, sign):
        return self.Get("/zodiac="+sign)

    def alquran(self):
        return self.Get("/alquran=list")

    def alquranQS(self, query):
        return self.Get("/alquran="+query)

    def bible(self):
        return self.Get("/bible")

    def adzan(self, cityname):
        return self.Get("/adzan="+cityname)

    def cuaca(self, cityname):
        return self.Get("/cuaca="+cityname)

    def bmkg(self):
        return self.Get("/bmkg")

    def corona(self):
        return self.Get("/corona")

    def karir(self):
        return self.Get("/karir")
 
    def cellular(self, query):
        return self.Get("/cell="+query)

    def lahir(self, date):
        return self.Get("/lahir="+date)

    def jadian(self, date):
        return self.Get("/jadian="+date)
 
    def nama(self, name):
        return self.Get("/nama="+name)

    def mimpi(self, query):
        return self.Get("/mimpi="+query)

    def acaratv(self):
        return self.Get("/acaratv/now")

    def acaratv_channel(self, channel):
        return self.Get("/acaratv="+channel)

    def cctv_code(self):
        return self.Get("/cctv/code")

    def cctvSearch(self, code):
        return self.Get("/cctv/search/id="+code)

    def mangaSearch(self, query):
        return self.Get("/manga/search="+query)

    def mangaChapter(self, chapterId):
        return self.Get("/manga/chapter="+chapterId)

    def timeline(self, url):
        return self.Get("/timeline="+url)

    def resi(self, query, code):
        return self.Get("/resi/"+query+"="+code)

    def screenshot(self, url):
        params = {"url": url }
        return self.Get("/screenshot", params=params)

    def gif(self, query):
        return self.Get("/gif="+query)

    def search(self, query):
        return self.Get("/search="+query)

    def calc(self, query):
        return self.Get("/calc="+query)

    def language(self):
        return self.Get("/language/code")

    def lineapp(self):
        return self.Get("/line")

    def linestore(self, packageId):
        params = {"id": packageId }
        return self.Get("/linestore", params=params)

    def lineqr(
        self,
        appName="DESKTOPWIN\t7.13.2\tWindows\t10.0",
        sysName="IMJUSTGOOD",
        cert=None
    ):
        headers = {
            "appName": appName,
            "sysName": sysName,
            "cert": cert
        }
        return self.Get("/lineqr", headers=headers)

    def lineqrGetPin(self, path):
        return self.Get("/pin"+path[30:])

    def lineqrGetToken(self, path):
        return self.Get("/token"+path[32:])

    def check_ip(self, query):
        return self.Get("/ip="+query)

    def proxies(self):
        return self.Get("/proxies")

    def BinaryEncode(self, query):
        params = {"q": query }
        return self.Get("/binary/text", params=params)

    def BinaryDecode(self, query):
        params = {"q": query }
        return self.Get("/binary/digit", params=params)

    def B64Encode(self, query):
        params = {"q": query }
        return self.Get("/base64/text", params=params)

    def B64Decode(self, query):
        params = {"q": query }
        return self.Get("/base64/code", params=params)

    def fancy(self, query):
        params = {"text": query }
        return self.Get("/fancy", params=params)

    def simisimi(self, query):
        params = {"text": query }
        return self.Get("/simisimi", params=params)

    def stamplist(self):
        return self.Get("/stamplist")

    def stamp(self, num, url):
        params = {"url": url, "num": num }
        return self.Get("/stamp", params=params)

    def meme(self, text1, text2, url):
        return self.Get("/meme/"+text1+"/"+text2+"/url="+url)

    def imagetext(self, query):
        params = {"text": query }
        return self.Get("/imgtext", params=params)

    def imgurl(self, path):
        file = {"file": open(path,"rb")}
        return self.Post("/imgurl",files=file)

    def ascii(self,query):
        result = self.Get("/ascii="+query)
        return result.text.split("pre")[1][1:-2]

    def customlink(self, label, url):
        return self.Get("/custom/make", headers={"label": label, "url": url})

    def watermark_image(self, imageUrl, iconUrl):
        params = {"image": imageUrl, "icon": iconUrl }
        return self.Get("/watermark/image", params=params)

    def watermark_text(self, imageUrl, text):
        params = {"image": imageUrl, "text": text }
        return self.Get("/watermark/text", params=params)

    def textpro(self, text1, text2=None, text3=None, effect="scifi"):
        params = {"effect": effect, "text1": text1, "text2": text2, "text3": text3 }
        return self.Get("/textpro", params=params)
