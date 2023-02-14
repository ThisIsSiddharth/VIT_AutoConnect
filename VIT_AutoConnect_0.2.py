import subprocess
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("VIT AutoConnect 0.02, Beta by Poppo")
print("Beginning connection protocols")
command_output = subprocess.run(["netsh", "wlan", "show", "networks"],capture_output = True).stdout.decode()
profile_names = (re.findall("VIT(.*)\r",command_output))
print(profile_names)
if (len(profile_names) != 0):
     if '2.4G' in profile_names:
          command_output = subprocess.run(["netsh", "wlan", "connect", "ssid=VIT5G", "name=VIT5G"],capture_output = True).stdout.decode()  
     elif '5G' in profile_names:
          command_output = subprocess.run(["netsh", "wlan", "connect", "ssid=VIT2.4G", "name=VIT2.4G"],capture_output = True).stdout.decode()
     elif '2.4' in profile_names:
          command_output = subprocess.run(["netsh", "wlan", "connect", "ssid=VIT5G", "name=VIT5G"],capture_output = True).stdout.decode()  
     elif '5' in profile_names:
          command_output = subprocess.run(["netsh", "wlan", "connect", "ssid=VIT2.4G", "name=VIT2.4G"],capture_output = True).stdout.decode()
else:
     print("The Desired Network was not found")
time.sleep(3)
try:
     PATH = r"C:\University\Projects\VIT_AutoConnect\chromedriver.exe"
     driver = webdriver.Chrome(PATH)
     driver.get("http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftconnecttest.com/redirect")
     try:
          search = driver.find_element_by_name("userId")
          search.send_keys("20BEC0785")
          search = driver.find_element_by_name("password")
          search.send_keys("WJZ8QB")
          submit = driver.find_element_by_name("Submit22")
          submit.click()
     except:
          print("I Believe you are already Connected to the network")
     time.sleep(2)
except:
     print("Srry, either you don't have the driver installed or it has not been updated")
#driver.quit()
#exit()
