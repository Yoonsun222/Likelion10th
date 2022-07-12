from bs4 import BeautifulSoup
import requests

url = "https://www.10000recipe.com/recipe/6971271"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


ko_title = soup.select_one('h3.ready_ingre3_tt > ul.case1 > li > a').get_text()  # 영화 title

print(ko_title)
#
# print('\n')
# score = soup.findAll('span', 'st_on')[0].text
# a, b, score = score.split(" ")
# print('관람객 평점: ', score) # 영화 평점
# print('\n')
#
# summary = list(soup.findAll('p', 'con_tx'))
# print("줄거리: ", summary[0].text)
# print('\n')
#
# # 영화 리뷰
# reviews = soup.findAll('div', 'score_reple')

# print('리뷰1: ', reviews[0].p.get_text().strip())
# print('\n')
# print('리뷰2: ', reviews[1].p.get_text().strip())
# print('\n')
# print('리뷰3: ', reviews[2].p.get_text().strip())
# print('\n')
# print("리뷰4: ", reviews[3].p.get_text().strip())
# print("\n")
# print("리뷰5:", reviews[4].p.get_text().strip())

for i in range(review_number):
    print('리뷰', i+1, ':', reviews[i].p.get_text().strip(), end = '\n\n') # 페이지에 리뷰가 5개 작성되어있으므로 6 이상의 수를 출력하면 error가 나온다.