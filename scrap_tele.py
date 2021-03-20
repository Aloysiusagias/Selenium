from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

myprofile = webdriver.FirefoxProfile(r'C:\Users\Aloysius\AppData\Roaming\Mozilla\Firefox\Profiles\fcbei8vp.teleScrape')
PATH = "C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox(firefox_profile=myprofile ,executable_path=PATH)

target = 1000

driver.get('https://web.telegram.org/#/im?p=@TheTradersGroup')
time.sleep(5)

wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
print(len(chat))

while len(chat) < target:
    html = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]')
    wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
    chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
    print(len(chat))
    driver.execute_script("arguments[0].scrollTop = 0", html)
penulis = ""
pesan2 = []
jam = ""
time.sleep(2)
for i in reversed(range(1,len(chat)+21)):
    if (len(driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(i)+"]")) > 0):
        time.sleep(0.25)
        pesan = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(i)+"]")
        driver.execute_script("arguments[0].scrollIntoView(true);", pesan)
        try:
            if (len(pesan.find_elements_by_xpath(".//a[@class='im_message_photo_thumb']")) > 0) :
                # print('ini adalah foto')
                penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
                if (len(pesan.find_elements_by_xpath(".//div[@class='im_message_photo_caption']")) > 0):
                    pesan2.insert(0, pesan.find_element_by_xpath(".//div[@class='im_message_photo_caption']").text)
                jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
            elif (len(pesan.find_elements_by_xpath(".//span[@ng-switch-when='messageActionChatJoined']")) > 0):
                # print('seseorang join')
                penulis = pesan.find_element_by_xpath(".//div[@class='im_service_message']").text
                pesan2 = []
                jam = ''
            elif (len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_split_text']")) > 0):
                if((len(pesan.find_elements_by_xpath(".//div[@class='im_message_date_split im_service_message_wrap' and @style='display: none;']")) > 0)):
                    penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
                    pesan2.insert(0, pesan.find_element_by_xpath(".//div[@class='im_message_text']").text)
                    jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
                else :
                    print("ini adalah tanggal")
                    print("Div : " + str(i))
                    print(pesan.find_element_by_xpath(".//span[@class='im_message_date_split_text']").text)
            else :
                # print('ini adalah pesan biasa')
                penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
                pesan2.insert(0, pesan.find_element_by_xpath(".//div[@class='im_message_text']").text)
                jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
        except:
            penulis = "Error"
            pesan2 = "Error"
        if(penulis != ""):
            # if(penulis == 'Hendro Masori'):
            #     print("Div : "+str(i))
            #     print("user : "+penulis)
            #     pesan2 = "\n".join(pesan2)
            #     print(pesan2)
            #     print("jam : " + jam)
            #     print('=======================================================')
            penulis = ""
            pesan2 = []
        jam = ""