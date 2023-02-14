import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("VIT AutoConnect 0.01 Beta by Poppo")
print("Beginning connection protocols")
command_output = subprocess.run(["netsh", "wlan", "connect", "ssid=VIT5", "name=VIT5"])
time.sleep(3)
PATH = r"C:\University\Projects\VIT_AutoConnect\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftconnecttest.com/redirect")
search = driver.find_element_by_name("userId")
search.send_keys("20BEC0785")
search = driver.find_element_by_name("password")
search.send_keys("WJZ8QB")
submit = driver.find_element_by_name("Submit22")
submit.click()
driver.close()
sys.exit()
