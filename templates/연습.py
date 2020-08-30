from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://place.map.kakao.com/26602826', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > div > a:nth-child(3) > span.color_b')
#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > div > a:nth-child(3) > span.color_b
#print(trs)

for tr in trs:
        rank = tr.select_one('a:nth-child(3) > span.color_b').text[0:2].strip()

        print(rank)

        # doc = {
        #     'rank': rank,
        #     'title': title,
        #     'artist': artist,
        #
        # }
