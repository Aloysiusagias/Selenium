from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://investasi.kontan.co.id/")
list = []
try:
    for n in range(1,6):
        link = '//*[@id="list-news"]/li['+str(n)+']/div[1]/div[2]/h1/a'
        driver.find_element_by_xpath(link).click()
        time.sleep(2)
        artikel = driver.find_element_by_class_name('tmpt-desk-kon')
        isi = artikel.find_elements_by_tag_name('p')
        judul = driver.find_element_by_class_name('detail-desk')
        berita = ''
        for n in range(1, len(isi)):
            berita = berita + isi[n].text
        item = {
            'judul' : judul.text,
            'link' : driver.current_url,
            'isi' : berita
        }
        list.append(item)
        driver.back()
    df = pd.DataFrame(list)
    print(df)
except: 
    print('error')
    driver.quit()
finally: 
    df.to_csv('datasetberita.csv', encoding='utf-8')
    driver.quit()