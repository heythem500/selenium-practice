import selenium
import webdriver_manager
from select import select
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select


driver = webdriver.Edge()
driver.get("http://localhost:3000/")

manar_ableToWrite = driver.find_element(By.CSS_SELECTOR, "[data-testid=email]").is_enabled()
print("is_enabled attribute = ", manar_ableToWrite)
manar_acces = driver.find_element(By.CSS_SELECTOR, "[data-testid=email]").accessible_name #rearly used in real life .. in Java it print: Email field not Email but both are lables
print("label/field is??", manar_acces)
driver.find_element(By.CSS_SELECTOR, "[data-testid=email]").send_keys("captin_manal@yahoo.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=password]").send_keys("4545454545")
driver.find_element(By.XPATH, "//*[@data-testid='password']").send_keys("4545454545Hs!") #must must use single quotes in Xpath
mananr_seeForm = driver.find_element(By.XPATH, "//*[@data-testid='submit']").is_displayed() #booles give true/false
print("we known that login button is displayed vlaue now =",mananr_seeForm)
driver.find_element(By.XPATH, "//*[@data-testid='submit']").click()
driver.implicitly_wait(5) #I must use this for the below code to work [wait time instead in java it looks like.. timeouts.implicitly_wait(Duration
driver.find_element(By.XPATH, "//*[@data-testid='complete-task']").click()
manar_boxCheckedOrNot = driver.find_element(By.XPATH, "//*[@data-testid='complete-task']").is_selected()
print("box is checked =",manar_boxCheckedOrNot)
""" ~since it can break the code sometimes after it runs 
manar_seeForm2 = driver.find_element(By.CSS_SELECTOR, "[data-testid=heythemProSoccer]").is_displayed()
print("can u see this element", manar_seeForm2) #it's normal here to give error but it won't print false .. however it can send false if the element exist in the code but hidden
"""
manar_AttributeIdName = driver.find_element(By.XPATH, "//*[@data-testid='complete-task']").get_attribute(name="type")#role from its name could be id, name, type, testid
print("the value of this attribute is:-",manar_AttributeIdName)
# manar_TagName = driver.find_element(By.XPATH, "//*[@data-testid='complete-task']").tag_name #its tag name = input
manar_TagName = driver.find_element(By.XPATH, "//*[@data-testid='delete']").tag_name #its tag name = button "example2 just to understood"
[print("get tagName as in java =",manar_TagName)]
manar_CssColor = driver.find_element(By.XPATH, "//*[@data-testid='todo-item']").value_of_css_property("background-color") #in a page after login u can use width, color, paddign any
print(manar_CssColor)
manar_XyAxis = driver.find_element(By.XPATH, "//*[@data-testid='todo-item']").location #get location of x and y axis, in java they get one of them only
print(manar_XyAxis)
manar_dimension = driver.find_element(By.XPATH, "//*[@data-testid='todo-item']").size #get dimentions height or width, also jave gives one like manar_dimension.width
print(manar_dimension)
manar_Rectangle = driver.find_element(By.XPATH, "//*[@data-testid='todo-item']").rect #similar to above but better has more info: x y width heigh
print(manar_Rectangle)
manar_role = driver.find_element(By.XPATH, "//*[@data-testid='complete-task']").aria_role #input type: button, checkbox, text etc..
print("role =",manar_role)



# ChatGpt fix
# input("Enter button to close")
driver.quit()
