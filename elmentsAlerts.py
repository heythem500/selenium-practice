from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://hatem-hatamleh.github.io/Selenium-html/alert.html")

#button 1
driver.find_element(By.CLASS_NAME, "alert").click()
kemo_alertTxtRead = driver.switch_to.alert.text
print(kemo_alertTxtRead)
time.sleep(0.80)
driver.switch_to.alert.accept() #click Enter on the popup

#button 2
driver.find_element(By.CLASS_NAME, "prompt").click()
driver.switch_to.alert.send_keys("Hello guys, can we meet today") #u can't see in on the browser but u see it on the console [but I couldn't in both ways!!]
time.sleep(0.50)
driver.switch_to.alert.accept()




time.sleep(15)









