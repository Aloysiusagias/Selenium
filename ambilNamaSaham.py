from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
saham = []

driver.get("https://www.idx.co.id/data-pasar/data-saham/daftar-saham/")
ibu = driver.find_element_by_xpath('//*[@id="stockTable"]/tbody')
anak = ibu.find_elements_by_tag_name('tr')

while (len(saham) != 722):
    time.sleep(1)
    ibu = driver.find_element_by_xpath('//*[@id="stockTable"]/tbody')
    anak = ibu.find_elements_by_tag_name('tr')
    for i in range(1,len(anak)+1):
        # item = driver.find_element_by_xpath('//*[@id="stockTable"]/tbody/tr['+str(i)+']/td[2]').text
        item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="stockTable"]/tbody/tr['+str(i)+']/td[2]')))
        item = item.text
        saham.append(item)
    # driver.find_element_by_xpath('//*[@id="stockTable_next"]').click()
    tombol = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="stockTable_next"]')))
    tombol.click()

print(saham)
