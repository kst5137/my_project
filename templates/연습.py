import requests
import json    # 파이썬 기본 모듈
import urllib  # 파이썬 기본 모듈
import pandas as pd
from pandas import DataFrame

api_key = "9744b0d293119837b040ed5eab047a75"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
session = requests.Session()
session.headers.update( {'User-agent': user_agent, 'referer': None, 'Authorization': 'KakaoAK ' + api_key} )

url_tpl = "https://dapi.kakao.com/v3/search/book"

q = "파이썬"    # 검색어
page = 1       # 접근할 페이지 번호(1~50)
size = 50      # 가져올 데이터 수 (1~80)

# 수집결과가 누적될 빈 리스트
documents = []

# 상위 100건을 가져오기 위해서는 한 페이지당 50건씩 2 페이지의 분량을 수집해야 한다.
for i in range(0, 2):
    # 페이지 번호 변수 준비
    page = i + 1

    # API에 전달할 파라미터
    params = {"page": page, "size": size, "query": q}
    query = urllib.parse.urlencode(params)
    # print(query)

    # 최종 접속 주소 구성하기
    api_url = url_tpl + "?" + query
    # print(api_url)

    # API 결과 가져오기
    r = session.get(api_url)

    if r.status_code != 200:
        print("[%d Error] %s" % (r.status_code, r.reason))
        quit()

    # 수집결과를 JSON으로 변경
    r.encoding = "utf-8"
    book_dict = json.loads(r.text)

    # 빈 리스트에 API에서 가져온 리스트를 병합
    documents += book_dict['documents']


    # 수집 결과를 데이터프레임으로 생성
    책검색df = DataFrame(documents)
    책검색df