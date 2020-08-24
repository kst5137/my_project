import simplejson,requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('template.html')


url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
apikey = "9744b0d293119837b040ed5eab047a75"
subj = "교촌치킨"
r = requests.get( url, params = {'query':subj}, headers={'Authorization' : 'KakaoAK ' + apikey } )
js = simplejson.JSONEncoder().encode(r.json())
for i in r.json()["documents"] :
    print (i["id"])
    print (i["place_name"])
    print (i["road_address_name"])
    print (i["phone"])




