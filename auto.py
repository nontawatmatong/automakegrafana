import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
#driver = webdriver.Chrome(executable_path = r'./usr/bin/chromedriver')


driver = webdriver.Firefox()
driver.get('https://bi.nopadol.com/login')
driver.fullscreen_window()

n = 0
time.sleep(n)

Username = "admin"
last = driver.find_element("xpath", '//*[@id="reactRoot"]/div[1]/main/div[3]/div/div[2]/div/div/form/div[1]/div[2]/div/div/input')
last.send_keys(Username)

time.sleep(n)

Pass = "itexpert"
last = driver.find_element("xpath", '//*[@id="current-password"]')
time.sleep(n)
last.send_keys(Pass,Keys.ENTER)

time.sleep(1)
