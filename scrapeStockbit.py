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

driver.get('https://stockbit.com/#/stream')