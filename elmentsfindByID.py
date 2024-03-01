from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select #works yet the one below is more commonly used
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.actions.interaction import #may remove now
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver import ActionChains





# import time

# With the help of chatGPT
# driver_path = r"E:\testing\coding files\PycharmProjects\hfiles\msedgedriver.exe"
# driver = webdriver.Edge(executable_path="E:\testing\coding files\PycharmProjects\hfiles\msedgedriver.exe")


driver = webdriver.Edge()
# Construct the absolute file path with raw string literal عشان مشكلة المسافات اللى في الفولدر
file_path = r"E:\testing\coding files\PycharmProjects\my first python with HatemQcart\hfiles\index.html"


# driver.get("https://www.msn.com")
driver.get("file:///" + file_path.replace("\\", "/"))
# driver.find_element(id("welcom")).
hasona_title= driver.title
print(hasona_title)
hasona_id = driver.find_element(By.ID, "welcome").text
print(hasona_id)
hasona_name = driver.find_element(By.NAME, "description").text
print(hasona_name)
hasona_class = driver.find_element(By.CLASS_NAME, "about").text
print("hasona_class = " + hasona_class)
hasona_tagName = driver.find_element(By.TAG_NAME, "li").text #triky watch tiny tags title on browser
print("tag name =",hasona_tagName)
hasona_linkTxt = driver.find_element(By.LINK_TEXT, "Go to About Page").text #if there's something beside like href="./about.html"
hasona_linkTxt2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Go to Ab").text #if there's something beside like href="./about.html"
print(hasona_linkTxt)
print(hasona_linkTxt2)
hasona_xpathTest = driver.find_element(By.XPATH, "/html/body/p[3]").text
print("Xpath Eample?? = ",hasona_xpathTest)
hasona_cs = driver.find_element(By.CSS_SELECTOR, ".list3").text #ex: id="welcome" or .+class but first word only or attributes but inside []
hasona_cs_v2 = driver.find_element(By.CSS_SELECTOR, "[data-testid=welcome-header]").text #if want second example .. name="description"
hasona_cs_v3 = driver.find_element(By.CSS_SELECTOR, ".course-list > .list5").text #direct parent to a child / but u can also remove >
print(hasona_cs)
print(hasona_cs_v2)
print("Css parent to child = " + hasona_cs_v3)
iD2Hsona = By.ID, "welcome" # in java he use By first like... By iD2Hsona = By.id("welcome");
iD4Hsona = driver.find_element(By.ID, "welcome") #another alternative that hatem used also
iD3Hsona = driver.find_element(*iD2Hsona).text
print("variable:::-" + iD3Hsona)
print(iD4Hsona.text)
hsona_MultipleElements = driver.find_elements(By.CSS_SELECTOR, ".course-list li") #not as in java hatem so I did my tweaks
print(hsona_MultipleElements[5].text)
print("Size of list chatGPT:",   len(hsona_MultipleElements)) #len in pyton vs size in java
hasona_DropMenu = Select(driver.find_element(By.ID, "courses")) #import Select first
hasona_DropMenu.select_by_index(2)
# hasona_DropMenu.select_by_visible_text("wdiocourse") #this or the one above works




# Wait for user input before closing the browser window  // will remain open until the user presses the Enter key in the terminal
input("Press Enter to close the browser...")
# time.sleep(2)
# driver.quit()

