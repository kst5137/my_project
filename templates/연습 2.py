import simplejson,requests
import sys
url = "https://dapi.kakao.com/v2/search/web"
apikey = "9744b0d293119837b040ed5eab047a75"
subj = "이효리"
r = requests.get( url, params = {'query':subj}, headers={'Authorization' : 'KakaoAK ' + apikey } )
js = simplejson.JSONEncoder().encode(r.json())
for i in r.json()["documents"] :
    print (i["title"])
    print (i["url"])
    print (i["datetime"])
    print (i["contents"])
