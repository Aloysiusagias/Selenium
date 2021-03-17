from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# driver.get('https://kumparan.com/kumparannews/kisruh-rapat-umum-pemegang-saham-pt-bcmg-bareskrim-tangkap-3-orang-1vLHH7WIw3S/full')
# isi = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]')
# isian = isi.find_elements_by_xpath("//span[@class='Textweb__StyledText-sc-1fa9e8r-0 laLMaB']")
# print(len(isian))
# for i in range(len(isian)):
#     print(isian[i].text)
# driver.quit()

driver.get('https://kumparan.com/topic/saham')
target = 150
list = []
ibu = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[2]/div[1]/div/div[1]')
artikel = ibu.find_elements_by_xpath("//div[@data-qa-id='news-item']")
window = driver.find_element_by_xpath('/html')
while (len(artikel) < target):
    ibu = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[2]/div[1]/div/div[1]')
    artikel = ibu.find_elements_by_xpath("//div[@data-qa-id='news-item']")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", window)
    print(len(artikel))
    time.sleep(1)

for i in range(1,target+1,2):
    penulis = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div['+str(i)+']/div/div/div[1]/a/div/div/div/div[2]/div/div[1]/span/div/span').text
    if (penulis!="Mohammad Teguh"):
        print(penulis)
    else:
        print('Ada si Teguh')