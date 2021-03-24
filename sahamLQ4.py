from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
saham = []
i = 1

driver.get('http://yuknabungsaham.idx.co.id/indeks-lq45')
while (len(saham) != 45):
    nama = driver.find_element_by_xpath('//*[@id="table_id"]/tbody/tr['+str(i)+']/td[2]').text
    i+=1
    saham.append(nama)

print(saham)