import simplejson,requests

url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
apikey = "9744b0d293119837b040ed5eab047a75"
subj = "교촌치킨"
r = requests.get( url, params = {'query':subj}, headers={'Authorization' : 'KakaoAK ' + apikey } )
js = simplejson.JSONEncoder().encode(r.json())
for i in r.json()["documents"] :
    print (i["id"])
    print (i["place_name"])
    print (i["road_address_name"])





