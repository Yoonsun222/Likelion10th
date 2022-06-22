from selenium import webdriver
import time 



options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome('C:/Users/profi/Downloads/chromedriver', options=options)
url = "https://naver.com"
browser.get(url)
browser.maximize_window()



#search_values = input()
search_values = '멋쟁이 사자처럼'
search_element = browser.find_element_by_id('query')
search_element.send_keys(search_values)
search_element.submit()



time.sleep(20)