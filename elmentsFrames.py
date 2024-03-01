from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
#page1
driver.get("https://hatem-hatamleh.github.io/Selenium-html/frames.html")
driver.switch_to.frame("qacart")
driver.find_element(By.XPATH, "//*[@name='firstName']").send_keys("ssffsfs@yahoo.com")
driver.switch_to.parent_frame() #if we need to get text/content from main page
print(driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(1)").text)
print(driver.find_element(By.XPATH, "//div[2]/p").text)# alterantive

# page 2
driver.get("https://hatem-hatamleh.github.io/Selenium-html/frame.html")
driver.switch_to.frame(driver.find_element(By.ID, "links"))
time.sleep(0.72)
driver.find_element(By.CLASS_NAME, "locators").click()
# driver.find_element(By.XPATH, "//a[@class='button actions']").click() #alternative
print("page title present:",driver.title)


# page3
time.sleep(2)
driver.get("https://www.w3.org/WAI/UA/TS/html401/cp0101/0101-FRAME-TEST.html")
driver.switch_to.frame("target1")
driver.find_element(By.LINK_TEXT, "Test Link 1").click()
print(driver.title)
driver.switch_to.default_content() #we must use this first to visit another frame vs frame
driver.switch_to.frame("head")
driver.find_element(By.LINK_TEXT, "References").click()



time.sleep(25)
driver.quit()