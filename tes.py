# a = " Baca juga"

# cari = "Baca jug"

# if cari in a :
#     print("ada")
# else :
#     print("tidak ada")

# if any(word in a for word in cari):
#     print("ada")
# else :
#     print("tidak ada")

# import re

# def findWholeWord(w):
#     return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

# hasil = findWholeWord('seek')('those who seek shall find')    # -> <match object>
# hasil2 = findWholeWord('word')('swordsmith')                   # -> None

# if(hasil2!=None):
#     print("ketemu")
# else :
#     print("Tidak ketemu")

# penulis = "Aloy"
# Berita = "ini Adalah contoh berita"

# f = open("scrape.txt","w+")
# f.write("Penulis : "+ penulis +"\nChat : "+Berita+"\n==========================\n")
# f.write("Penulis : "+ penulis +"\nChat : "+Berita+"\n==========================\n")
# f.close()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://money.kompas.com/read/2021/03/24/194729926/bantah-selundupkan-baja-dari-china-bos-krakatau-steel-tuduhan-yang-sangat')
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[4]/div[2]/div[6]/div/div[3]/a').click()