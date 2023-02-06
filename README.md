## API.IMJUSTGOOD.COM
```
█ █▀▄▀█  ▀█ █  █ █▀▀▀ ▀▀█▀▀ █▀▀▀ █▀▀█ █▀▀█ █▀▀▄
█ █ ▀ █ ▄▄█ █▄▄█ ▄▄▄█   █   █▄▄█ █▄▄█ █▄▄█ █▄▄▀
API MEDIA SERVICE TO MAKE YOUR CODE MORE BETTER.
```
<p>
    <a href="http://pypi.org/project/justgood" rel="nofollow">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/justgood?label=PyPI" style="max-width:100%;">
    </a>
    <a href="https://github.com/RendyTR/api.imjustgood.com" rel="nofollow">
        <img alt="Update" src="https://img.shields.io/github/last-commit/rendytr/api.imjustgood.com?color=red&label=Update" height="20" style="max-width:100%;">
    </a>
    <a href="https://github.com/RendyTR" rel="nofollow">
        <img alt="Views" src="https://komarev.com/ghpvc/?username=RendyTR&color=green&label=Views" height="20" style="max-width:100%;">
    </a>
</p>

Full documentation available <a href="https://api.imjustgood.com/">here</a>

### Installation
```
pip3 install justgood
```

### Upgrade
```
pip3 install --upgrade justgood
```

### Documentation
You need <a href="https://api.imjustgood.com/intro">apikey</a> to authenticate calling our program.<br>
Here is how to use the module in your own python code. we choose <a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/instagram_post.py">instapost</a> media as an example.
```python
from justgood import imjustgood

api   =  imjustgood("INSERT_YOUR_APIKEY_HERE")
data  =  api.instapost("https://.instagram.com/p/Cg74iKsBBc2/")

print(data)
```

[ 2OO ] Response Success
```json
{
    "creator": "Imjustgood",
    "result": {
        "caption": "GET STARTED NOW\nhttps://api.imjustgood.com\n#api #bot #pypi #coder #programmer",
        "comments": "0",
        "created": "5 months ago",
        "fullname": "The Autobots Corporation",
        "likes": "3",
        "picture": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/272003703_1108244669995347_1136634152614637195_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_ohc=zdEObJxmKCUAX9S4iAR&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfDHmFkCgpIGfI-N5wQyvarDSMLQuT59GhAAY0hmJfMEug&oe=63B9CB82&_nc_sid=4f375e",
        "postData": [
            {
                "postUrl": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/297855880_804422890580244_3970587908499851308_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=100&_nc_ohc=FIePBkvAxicAX9iV9sf&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfDRbS-OZxDXeYK0ea_kHvfbdCxsIEx-Vjo5BlwStxoXBQ&oe=63B93908&_nc_sid=4f375e",
                "poster": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/297855880_804422890580244_3970587908499851308_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=100&_nc_ohc=FIePBkvAxicAX9iV9sf&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfDRbS-OZxDXeYK0ea_kHvfbdCxsIEx-Vjo5BlwStxoXBQ&oe=63B93908&_nc_sid=4f375e",
                "type": "image"
            },
            {
                "postUrl": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/297518102_151529124202237_7924946476954369740_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=101&_nc_ohc=SYtZTBJneuwAX8ZjfAl&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfDLfmQeKhj59gB4x8IXcyuB6ZXu4tY8rQuzUC7AyBj-Cg&oe=63B95A18&_nc_sid=4f375e",
                "poster": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/297518102_151529124202237_7924946476954369740_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=101&_nc_ohc=SYtZTBJneuwAX8ZjfAl&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfDLfmQeKhj59gB4x8IXcyuB6ZXu4tY8rQuzUC7AyBj-Cg&oe=63B95A18&_nc_sid=4f375e",
                "type": "image"
            },
            {
                "postUrl": "https://scontent-iad3-2.cdninstagram.com/v/t50.2886-16/298161345_1019698588712326_4289148637928675103_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLjY0MC5jYXJvdXNlbF9pdGVtLmJhc2VsaW5lIiwicWVfZ3JvdXBzIjoiW1wiaWdfd2ViX2RlbGl2ZXJ5X3Z0c19vdGZcIl0ifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=110&_nc_ohc=O4hX3emjkcIAX8Uk3oZ&tn=3OBlyBWCNXe0Z2Yw&edm=AP_V10EBAAAA&vs=584342153190694_3179117251&_nc_vs=HBksFQAYJEdNR1V4UkdHZlNnVWFaOERBQi1YbGhqMkhZWTdia1lMQUFBRhUAAsgBABUAGCRHRlpRdnhINW1YWnY5M2tCQUx3X3dRUnUxQk5pYmtZTEFBQUYVAgLIAQAoABgAGwGIB3VzZV9vaWwBMBUAACbmm5idj%2BXnPxUCKAJDMywXQCtU%2FfO2RaIYEmRhc2hfYmFzZWxpbmVfMV92MREAde4HAA%3D%3D&ccb=7-5&oh=00_AfBmGM0IMbYbspzTCoQutGDRJud2jKqtOsR7p3AjhUpWuQ&oe=63B63D86&_nc_sid=4f375e",
                "poster": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/297833882_144728104900625_5890250235783357340_n.jpg?stp=dst-jpg_e15&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=105&_nc_ohc=uRKv0ulupYgAX93jqv9&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfAryUwU7X981CR-XZPRokqS3MO9f-ygfv8KCLfr2s2dKg&oe=63B9B217&_nc_sid=4f375e",
                "type": "video"
            }
        ],
        "postType": "post",
        "private": false,
        "slidePost": true,
        "username": "the.autobots_corp",
        "verified": false
    },
    "status": 200
}
```

Get certain attributes
```
>>> username = data["result"]["username"]
>>> print(username)
the.autobots_corp

>>> fullname = data["result"]["fullname"]
>>> print(fullname)
The Autobots Corporation

>>> created = data["result"]["created"]
>>> print(created)
5 months ago

>>> caption = data["result"]["caption"]
>>> print(caption)
GET STARTED NOW
https://api.imjustgood.com
#api #bot #pypi #coder #programmer

>>> picture = data["result"]["picture"]
>>> print(picture)
https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/272003703_1108244669995347_1136634152614637195_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_ohc=zdEObJxmKCUAX9S4iAR&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfDHmFkCgpIGfI-N5wQyvarDSMLQuT59GhAAY0hmJfMEug&oe=63B9CB82&_nc_sid=4f375e

>>> for a in data["result"]["postData"]:
...     print(a["type"], a["postUrl"])
image https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/297855880_804422890580244_3970587908499851308_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=100&_nc_ohc=FIePBkvAxicAX9iV9sf&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfDRbS-OZxDXeYK0ea_kHvfbdCxsIEx-Vjo5BlwStxoXBQ&oe=63B93908&_nc_sid=4f375e
image https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/297518102_151529124202237_7924946476954369740_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=101&_nc_ohc=SYtZTBJneuwAX8ZjfAl&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfDLfmQeKhj59gB4x8IXcyuB6ZXu4tY8rQuzUC7AyBj-Cg&oe=63B95A18&_nc_sid=4f375e
video https://scontent-iad3-2.cdninstagram.com/v/t50.2886-16/298161345_1019698588712326_4289148637928675103_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLjY0MC5jYXJvdXNlbF9pdGVtLmJhc2VsaW5lIiwicWVfZ3JvdXBzIjoiW1wiaWdfd2ViX2RlbGl2ZXJ5X3Z0c19vdGZcIl0ifQ&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=110&_nc_ohc=O4hX3emjkcIAX8Uk3oZ&tn=3OBlyBWCNXe0Z2Yw&edm=AP_V10EBAAAA&vs=584342153190694_3179117251&_nc_vs=HBksFQAYJEdNR1V4UkdHZlNnVWFaOERBQi1YbGhqMkhZWTdia1lMQUFBRhUAAsgBABUAGCRHRlpRdnhINW1YWnY5M2tCQUx3X3dRUnUxQk5pYmtZTEFBQUYVAgLIAQAoABgAGwGIB3VzZV9vaWwBMBUAACbmm5idj%2BXnPxUCKAJDMywXQCtU%2FfO2RaIYEmRhc2hfYmFzZWxpbmVfMV92MREAde4HAA%3D%3D&ccb=7-5&oh=00_AfBmGM0IMbYbspzTCoQutGDRJud2jKqtOsR7p3AjhUpWuQ&oe=63B63D86&_nc_sid=4f375e
```

### More Media Fitures
<table>
    <tbody>
        <tr>
            <td>Apikey Status</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/apikey_status.py">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/youtube_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/youtube_downloader.py">Example</a></td>
        </tr>
        <tr>
            <td>Joox Music</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/joox_music.py">Example</a></td>
        </tr>
        <tr>
            <td>Lyric Finder</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/lyric_finder.py">Example</a></td>
        </tr>
        <tr>
            <td>Chord Guitar Finder</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/chord_guitar_finder.py">Example</a></td>
        </tr>
        <tr>
            <td>Smule Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/smule_profile.py">Example</a></td>
        </tr>
        <tr>
            <td>Smule Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/smule_downloader.py">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/tiktok_profile.py">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/tiktok_downloader.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/instagram_profile.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Post</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/instagram_post.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Story</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/instagram_story.py">Example</a></td>
        </tr>
        <tr>
            <td>Twitter Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/twitter_profile.py">Example</a></td>
        </tr>
        <tr>
            <td>Twitter Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/twitter_downloader.py">Example</a></td>
        </tr>
        <tr>
            <td>Facebook Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/facebook_downloader.py">Example</a></td>
        </tr>
        <tr>
            <td>Pinterest Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/pinterest_downloader.py">Example</a></td>
        </tr>
        <tr>
            <td>Snackvideo Downloader</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/snackvideo_downloader.py">Example</a></td>
        </tr>
        <tr>
            <td>GitHub Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/github_profile.py">Example</a></td>
        </tr>
        <tr>
            <td>Secreto Profile</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/secreto_profile.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE Secondary</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/line_secondary.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE Voom</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/line_voom.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE Sticker Store</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/line_sticker_store.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE App Version</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/line_app_version.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/google_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Image</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/google_image.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Playstore</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/google_playstore.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Translate</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/google_translate.py">Example</a></td>
        </tr>
        <tr>
            <td>Random Proxies</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/random_proxies.py">Example</a></td>
        </tr>
        <tr>
            <td>Wallpaper HD</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/wallpaper.py">Example</a></td>
        </tr>
        <tr>
            <td>Porn Videos</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/porn.py">Example</a></td>
        </tr>
        <tr>
            <td>Pornstar</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/pornstar.py">Example</a></td>
        </tr>
        <tr>
            <td>Hentai</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/hentai.py">Example</a></td>
        </tr>
        <tr>
            <td>Kamasutra</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/kamasutra.py">Example</a></td>
        </tr>
        <tr>
            <td>Dick Analyze</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/dick_analyze.py">Example</a></td>
        </tr>
        <tr>
            <td>Tits Analyze</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/tits_analyze.py">Example</a></td>
        </tr>
        <tr>
            <td>Vagina Analyze</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/vagina_analyze.py">Example</a></td>
        </tr>
        <tr>
            <td>Meme Generator</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/meme_generator.py">Example</a></td>
        </tr>
        <tr>
            <td>Movie Review</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/movie_review.py">Example</a></td>
        </tr>
        <tr>
            <td>Movie Quotes</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/movie_quotes.py">Example</a></td>
        </tr>
        <tr>
            <td>Cinema 21</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/cinema_21.py">Example</a></td>
        </tr>
        <tr>
            <td>TinyUrl</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/tinyurl.py">Example</a></td>
        </tr>
        <tr>
            <td>Bit.ly</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/bitly.py">Example</a></td>
        </tr>
        <tr>
            <td>KBBI</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/kbbi.py">Example</a></td>
        </tr>
        <tr>
            <td>Top News</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/top_news.py">Example</a></td>
        </tr>
        <tr>
            <td>Wikipedia</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/wikipedia.py">Example</a></td>
        </tr>
        <tr>
            <td>Urban Dictionary</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/urban_dictionary.py">Example</a></td>
        </tr>
        <tr>
            <td>Zodiac Daily</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/zodiac_daily.py">Example</a></td>
        </tr>
        <tr>
            <td>Al-Qur'an</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/alquran.py">Example</a></td>
        </tr>
        <tr>
            <td>Bible</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/bible.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Waktu Sholat</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/info_waktu_sholat.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Cuaca Dunia</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/info_cuaca_dunia.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Gempa BMKG</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/info_gempa_bmkg.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Corona Virus</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/info_corona_virus.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Lowongan Kerja</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/info_lowongan_kerja.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Resi Pengiriman</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/info_resi_pengiriman.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Phone Cellular</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/info_phone_cellular.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Lahir</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/info_tanggal_lahir.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Jadian</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/info_tanggal_jadian.py">Example</a></td>
        </tr>
        <tr>
            <td>Arti Nama</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/arti_nama.py">Example</a></td>
        </tr>
        <tr>
            <td>Arti Mimpi</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/arti_mimpi.py">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Sekarang</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/acara_tv_sekarang.py">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Stasiun</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/acara_tv_stasiun.py">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Code</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/cctv_camera_code.py">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/cctv_camera_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Manga Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/manga_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Manga Chapter</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/manga_chapter.py">Example</a></td>
        </tr>
        <tr>
            <td>Calculator</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/calculator.py">Example</a></td>
        </tr>
        <tr>
            <td>Check IP Address</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/check_ip_address.py">Example</a></td>
        </tr>
        <tr>
            <td>Binary Encode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/binary_encode.py">Example</a></td>
        </tr>
        <tr>
            <td>Binary Decode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/binary_decode.py">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Encode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/base64_encode.py">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Decode</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/base64_decode.py">Example</a></td>
        </tr>
        <tr>
            <td>Screenshot Web</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/screenshot_web.py">Example</a></td>
        </tr>
        <tr>
            <td>ASCII Text</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/ascii_text.py">Example</a></td>
        </tr>
        <tr>
            <td>Fancy Text</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/fancy_text.py">Example</a></td>
        </tr>
        <tr>
            <td>Customize URL</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/customize_url.py">Example</a></td>
        </tr>
        <tr>
            <td>GIF Search</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/gif_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Convert Image to URL</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/convert_image_to_url.py">Example</a></td>
        </tr>
        <tr>
            <td>Convert Text to Image</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/convert_text_to_image.py">Example</a></td>
        </tr>
        <tr>
            <td>Watermark Text</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/watermark_text.py">Example</a></td>
        </tr>
        <tr>
            <td>Watermark Image</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/watermark_image.py">Example</a></td>
        </tr>
        <tr>
            <td>SimiSimi</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/simisimi_chats.py">Example</a></td>
        </tr>
        <tr>
            <td>Stamp Image</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/stamp_image.py">Example</a></td>
        </tr>
        <tr>
            <td>TextPro</td>
            <td>Active</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/example/textpro.py">Example</a></td>
        </tr>
    </tbody>
</table>

### Contact us
* <a href="https://imjustgood.com/team">IMJUSTGOOD TEAM</a>
