import requests
import re
from bs4 import BeautifulSoup

url = "https://place.map.kakao.com/24769004"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

placereview = soup.find("p", attrs={"class":"txt_comment"})
if placereview:
    placereview = placereview.get_text
else:
    placereview = "평점없음"
print(placereview)