from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.cnnindonesia.com/tag/saham")
target = 100
list = []
mainn = driver.find_element_by_id('content')
news = mainn.find_elements_by_tag_name('article')
print(len(news))
a = len(news)
while a < target+20:
    window = driver.find_element_by_xpath('/html')
    driver.execute_script("return arguments[0].scrollIntoView(true);", window)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/a').click()
    mainn = driver.find_element_by_id('content')
    news = mainn.find_elements_by_tag_name('article')
    print(len(news))
    a = len(news)
    time.sleep(1)

for i in range(1,target+1):
    link = '//*[@id="content"]/div/div[2]/div/div[1]/article[' + str(i) + ']/a'
    tipe = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[1]/article['+ str(i)+']/a/span[2]/span[2]').text
    print(tipe)
    if (tipe != 'TV'):
        a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, link))).get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(a)
        # driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[1]/article[' + str(i) +']/a').click()
        try :
            artikel = driver.find_element_by_id('detikdetailtext')
        except :
            print('error')
            artikel = driver.find_element_by_id('content')
        isi = artikel.find_elements_by_tag_name('p')
        berita = ''
        for n in range(len(isi)):
            berita = berita + isi[n].text + ' '
        judul = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[1]/h1').text
        print(str(i) + '. ' + judul)
        item = {
            'judul' : judul,
            'link' : driver.current_url,
            'isi' : berita
        }
        list.append(item)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print('selesai')
    else :
        target += 1
df = pd.DataFrame(list)
print(df)
df.to_csv('dataset_cnn.csv', encoding='utf-8')
driver.quit()