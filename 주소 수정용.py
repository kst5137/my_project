from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# id = request.form['id_give']
# data = requests.get('https://place.map.kakao.com/'+id, headers=headers)
# html = BeautifulSoup(data.text, 'html.parser')


app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('template2.html')


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({}, {'_id': 0}))
    # 1. 모든 reviews의 문서를 가져온 후 list로 변환합니다.
    return jsonify({'result': 'success', 'reviews': reviews})


@app.route('/review', methods=['POST'])
def write_review():
    # title_receive로 클라이언트가 준 title 가져오기
    name_receive = request.form['name_give']
    # author_receive로 클라이언트가 준 author 가져오기
    address_receive = request.form['address_give']
    # review_receive로 클라이언트가 준 review 가져오기
    phone_receive = request.form['phone_give']
    id_receive = request.form['id_give']
    x_receive = request.form['x_give']
    y_receive = request.form['Y_give']
    scoresum_receive = request.form['scoresum_give']
    scorecnt_receive = request.form['scoresum_cnt']

    # DB에 삽입할 review 만들기
    review = {
        'name': name_receive,
        'address': address_receive,
        'phone': phone_receive,
        'id': id_receive,
        'x': x_receive,
        'y': y_receive,
        'scoresum': scoresum_receive,
        'scorecnt': scorecnt_receive
    }
    # reviews에 review 저장하기
    db.reviews.insert_one(review)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)