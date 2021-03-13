from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://kumparan.com/kumparannews/kisruh-rapat-umum-pemegang-saham-pt-bcmg-bareskrim-tangkap-3-orang-1vLHH7WIw3S/full')
# content = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'content')))
isi = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]')
# isi = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'StoryRenderer__EditorWrapper-mnwwoh-0 gZLNBF')))
# isian = isi.find_elements_by_class_name('Textweb__StyledText-sc-1fa9e8r-0 laLMaB')
isian = isi.find_elements_by_xpath("//span[@class='Textweb__StyledText-sc-1fa9e8r-0 laLMaB']")
print(len(isian))
for i in range(len(isian)):
    print(isian[i].text)
driver.quit()