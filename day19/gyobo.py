from selenium import webdriver
from bs4 import BeautifulSoup
import time as t


# 날짜처리 라이브러리
from datetime import datetime

# 엑셀저장 라이브러리 
import xlsxwriter

# 이미지 다운로드 처리 라이브러리
import urllib.request as req
from io import BytesIO

# 오늘 날짜 시간 
d = datetime.today()

# 파일명
file_name = f'교보문고베스트셀러_{d.year}_{d.month}_{d.day}.xlsx'

# 파일 저장 경로
file_save_path = f'D:/isec_kgw/py_study/{file_name}'

# 엑셀라이브러리 객체 생성
workbook = xlsxwriter.Workbook(file_save_path)

# 엑셀 워크 시트 만들기
worksheet = workbook.add_worksheet()

# 행 꾸미기 방법
styles = {
    'bold' : True,
    'font_color' : 'red',
    'bg_color' : 'yellow'
}
cell_format = workbook.add_format(styles)

# 엑셀 열이름 (첫줄 정보 생성)
worksheet.write('A1', '순위', cell_format)
worksheet.write('B1', '썸네일',cell_format)
worksheet.write('C1', '책이름',cell_format)
worksheet.write('D1', '가격',cell_format)
worksheet.write('E1', '저자',cell_format)


# 물리드라이버
browser = webdriver.Chrome('D:/isec_kgw/py_study/c_driver/chromedriver.exe')

# 브라우저 최대창으로 띄우기
# browser.maximize_window()

# 브라우저 원하는 사이즈로 키우기
browser.set_window_size(1280,1080)

# 타겟 사이트로 이동
browser.get('http://www.kyobobook.co.kr/index.laf')


########## 핵심 로직 ############

t.sleep(2)

browser.find_element_by_css_selector('#header > div.navigation_bar > ul.gnb_main.add_1 > li.item_1 > a').click()

t.sleep(2)

browser.find_element_by_css_selector('#bestSeller > div.section.first.on > div > div > a > img').click()


# 현재 페이지 소스코드 불러오기
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

prod_list = soup.select('ul.list_type01 > li')

rank = 1
'''
for n in range(2,11):
        
    if n > 1:
        browser.find_element_by_css_selector(f'#main_contents > div:nth-child(6) > div.list_paging > ul > li:nth-child({n}) > a').click()

    t.sleep(2)
'''    
for i in range(20):

    p = prod_list[i]

    img_tag = p.select_one('.cover > a > img')
    img_src = img_tag['src']
    prod_name = p.select_one('.title > a > strong').text.strip()
    prod_price = p.select_one('.price > strong').text.strip()
    prod_author = p.select_one('.author').text.strip()
    author_plus = prod_author.split('|')
    author = author_plus[0]

    

    print(prod_name)
    print(prod_price)
    print(author.strip())
    print('='*40)

    worksheet.write(f'A{rank+1}', rank)
    img_data = BytesIO(req.urlopen(img_src).read())
    worksheet.insert_image(f'B{rank+1}', img_src, {'image_data': img_data}) # 셀이름, 이미지위치, 딕셔너리 
    worksheet.write(f'C{rank+1}', prod_name)
    worksheet.write(f'D{rank+1}', prod_price)
    worksheet.write(f'E{rank+1}', author)

    rank += 1
    

browser.close()
workbook.close()