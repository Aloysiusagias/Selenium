from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://id.investing.com/news/stock-market-news')
time.sleep(3)
bungkus = driver.find_element_by_xpath('//*[@id="leftColumn"]/div[4]')
jumlah = bungkus.find_elements_by_tag_name('article')
print(len(jumlah))
for j in range(2):
    for i in range(1,len(jumlah)+1):
        artikel1 = driver.find_element_by_xpath('//*[@id="leftColumn"]/div[4]/article['+str(i)+']')
        judul = driver.find_element_by_xpath('//*[@id="leftColumn"]/div[4]/article['+str(i)+']/div[1]/a').text
        if("js-article-item articleItem   " == artikel1.get_attribute('class')):
            print(judul + " Bisa di scrape")
        else :
            print(judul + " Tidak Bisa di scrape")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i'))).click()
    driver.find_element_by_xpath('//*[@id="paginationWrap"]/div[3]/a').click()
    time.sleep(3)