from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://investasi.kontan.co.id/news/harga-emas-turun-simak-rekomendasi-analis")

artikel = driver.find_element_by_class_name('tmpt-desk-kon')
isi = artikel.find_elements_by_tag_name('p')
judul = driver.find_element_by_class_name('detail-desk')
berita = ''
for n in range(1, len(isi)):
    if(isi[n].text[:9] != "Baca Juga"):
        berita = berita + isi[n].text + ' '
print(berita)
driver.quit()