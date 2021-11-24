
# 셀레늄 : 웹 자동화 및 웹의 소스코드를 수집하는 모듈
from selenium import webdriver # 셀레늄 모듈 로딩
import time as t

# 크롬 브라우저 물리드라이버 가동

browser = webdriver.Chrome('D:/isec_kgw/py_study/c_driver/chromedriver.exe')

# 원하는 사이트로 이동
browser.get('https://news.daum.net/society#1')



for n in range(1, 4):
    for m in range(1,11):
        if m == 1:
            rank1 = browser.find_element_by_xpath(f'//*[@id="mAside"]/div[1]/ul/li[{n}]/div/ol[1]/li[{m}]/strong/a')
            rank1.click()
            t.sleep(2)

    


