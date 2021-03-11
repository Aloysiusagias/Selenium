from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://investasi.kontan.co.id/")
target = 200
list = []
isi = driver.find_element_by_id('list-news')
artikel = isi.find_elements_by_tag_name('li')
window = driver.find_element_by_xpath('/html')
while (len(artikel) < target):
    isi = driver.find_element_by_id('list-news')
    artikel = isi.find_elements_by_tag_name('li')
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", window)
    print(len(artikel))
driver.execute_script("return arguments[0].scrollIntoView(true);", window)
for i in range(1,target+1):
    link = '//*[@id="list-news"]/li['+str(i)+']/div[1]/div[2]/h1/a'
    a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, link))).get_attribute('href')
    # print(str(i) + '. '+a)
    driver.execute_script("window.open('');") #open new tab
    driver.switch_to.window(driver.window_handles[1]) #berpindah
    driver.get(a)
    artikel = driver.find_element_by_class_name('tmpt-desk-kon')
    isi = artikel.find_elements_by_tag_name('p')
    judul = driver.find_element_by_class_name('detail-desk')
    berita = ''
    for n in range(1, len(isi)):
        if(isi[n].text[:9] != "Baca Juga"):
            berita = berita + isi[n].text + ' '
    item = {
        'judul' : judul.text,
        'link' : driver.current_url,
        'isi' : berita
    }
    list.append(item)
    print(str(i)+'. ' +judul.text)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print('selesai')
df = pd.DataFrame(list)
print(df)
df.to_csv('dataset_kontan.csv', encoding='utf-8')
driver.quit()