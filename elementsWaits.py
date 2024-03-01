from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Edge()
driver.get("https://hatem-hatamleh.github.io/Selenium-html/wait.html")

#Implicit waits
driver.implicitly_wait(5) #maximum time till u find all the elements requestd during seasion not just the first one
driver.find_element(By.CLASS_NAME, "primary").click()
# driver.find_element(By.CSS_SELECTOR, ".button.primary").click() #alternative

#Explicit waits
# driver.get("https://hatem-hatamleh.github.io/Selenium-html/wait.html")
driver.refresh()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "primary"))).click() #we use another tuple ()
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "cover"))) #see the cover first [other coders works find witouh this line can remove but may need later]
wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "cover"))) #when this element "the cover square" become hidden do the line below
driver.find_element(By.CLASS_NAME, "secondary").click()





input("Enter button to close")
driver.quit()