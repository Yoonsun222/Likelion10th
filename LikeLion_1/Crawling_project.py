from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome('C:/Users/profi/Downloads/chromedriver', options=options)
url = "https://movie.naver.com/"
browser.get(url)
browser.maximize_window()

name = input()

time.sleep(1)
b_element = browser.find_element_by_id('ipt_tx_srch')
b_element.send_keys(name)

time.sleep(1)
b_click = browser.find_element_by_class_name('btn_srch')
b_click.click()


b_click = browser.find_element_by_class_name('result_thumb')
b_click.click()


html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')


results = soup.findAll('span','st_on')
time.sleep(1)

print()

print('제목 :', name ,'\n')

score  = soup.find_all('span','st_on')
txt1,txt2,score = score[0].text.split(" ")
print('관객 평점 :', score,'\n')


t_story = soup.find('h5','h_tx_story')
c_story = soup.find('p','con_tx')
h_story = t_story.text + " " + c_story.text

print('줄거리 :', h_story,'\n')

review = soup.find_all('div','score_reple')




for i,content in enumerate(review):
    print(f'리뷰{i+1} :',content.p.text.strip(),'\n')