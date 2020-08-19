from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://map.kakao.com/?from=total&nil_suggest=btn&q=교촌치킨&tab=place', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select(" #info\.search\.place\.list > li.PlaceItem.clickArea.PlaceItem-ACTIVE")
#info\.search\.place

print(trs)

# for tr in trs:
#         name = tr.select_one('div.head_item.clickArea > strong > a.link_name > strong').text[0:2].strip()
# info\.search\.place\.list > li.PlaceItem.clickArea.PlaceItem-ACTIVE > div.head_item.clickArea > strong > a.link_name
#
#         address = tr.select_one('div.info_item > div.addr > p').text.strip()
#         # info\.search\.place\.list > li:nth-child(2) > div.info_item > div.addr > p:nth-child(1) (주소)
#info\.search\.place\.list > li.PlaceItem.clickArea.PlaceItem-ACTIVE > div.info_item > div.addr > p:nth-child(1)
for tr in trs:
    # movie 안에 a 가 있으면,
    name = tr.select_one('div.head_item.clickArea > strong > a.link_name')
    # td 안에 a 하나 밖에 없으니까 div 빼고 'td.title a'도 가능하지만 예외 처리할때 힘듬
    if name is not None:  # 이런게 까다롭기 때문에 확인을 잘 해줘야한 10번째 마다 none값이라 그냥 하면 오류뜰것
        # a의 text를 찍어본다.
        address = tr.select_one('div.info_item > div.addr > p').text

    print(name,address)


# 구글 굴다리소곱창(체인 x)
#tsuid22 > span > div > div > div.kp-header > div.fYOrjf.kp-hc > div.Hhmu2e.mod.NFQFxe.viOShc.LKPcQc > div > div.SPZz6b > h2 > span
# 구글 교촌치킨
# rso > div:nth-child(2) > div > div.AEprdc.vk_c > div > div:nth-child(4) > div.ccBEnf > div:nth-child(1) > div > div > a.C8TUKc.CNIbvd.rllt__link.a-no-hover-decoration > div > div.dbg0pd > span
# 구글 프리모바치오바치
#rso > div:nth-child(1) > div > div.AEprdc.vk_c > div > div:nth-child(4) > div.ccBEnf > div:nth-child(1) > div > div > a > div > div.dbg0pd > spanx

#네이버 교촌치킨
#loc-main-section-root > div > div.place_section_content_nx > div:nth-child(2) > ul > li:nth-child(1) > div._75bjI > div._2LKql > a > mark
#네이버 굴다리 소곱창
#place_main_ct > div > div > div > div.ct_box_area > div.biz_name_area > a

#다음 굴다리 소곱창
#info\.search\.place\.list > li:nth-child(1) > div.head_item.clickArea > strong > a.link_name > strong (카카오맵)
#poiColl > div.coll_cont.poi_cont > div.wrap_place > ul > li:nth-child(1) > div.cont_info > div > a > b:nth-child(1)
#다음 교촌치킨
#poiColl > div.coll_cont.poi_cont > div.wrap_place > ul > li:nth-child(1) > div.cont_info > div > a.fn_tit > b
#교촌치킨 카카오맵
#info\.search\.place\.list > li:nth-child(2) > div.head_item.clickArea > strong > a.link_name > strong (이름)
#info\.search\.place\.list > li:nth-child(2) > div.info_item > div.addr > p:nth-child(1) (주소)
#info\.search\.place\.list > li:nth-child(1) > div.head_item.clickArea > strong > a.link_name > strong (이름)
#info\.search\.place\.list > li:nth-child(1) > div.info_item > div.addr > p:nth-child(1) (주소)

