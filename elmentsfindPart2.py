#page part2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


driver = webdriver.Edge()
file_path = r"E:\testing\coding files\PycharmProjects\my first python with HatemQcart\hfiles\index.html"


# driver.get("https://www.msn.com")
driver.get("file:///" + file_path.replace("\\", "/"))

driver.maximize_window()

#note: class name breaks+couldn't locate the item / CSS_SELECTOR don't break but didn't apply the action
ActionChains(driver).double_click(driver.find_element(By.XPATH, "//input[@value='Click me']")) #must use ActionChains(driver).dou -- instead of ActionChains.double_click
action = ActionChains(driver) #we can also use var and remove the word ActionChains(driver) to be action.double_click(driver.find_element(By.XPATH, "//input[@value='Cli me']")).perform()
action.context_click(driver.find_element(By.XPATH, "//input[@value='Click me']")).perform() #this an order for the mouse to click right click = context_click
action.move_to_element(driver.find_element(By.CLASS_NAME, "trigger")).perform() #also works with css .trigger / thid action stimulate putting the mouse on button without clicking


#darg and drop from left to right
canada_source = driver.find_element(By.CLASS_NAME, "example-draggable")
canada_destination = driver.find_element(By.CLASS_NAME, "example-dropzone")
action.drag_and_drop(canada_source, canada_destination).perform()
action.click_and_hold(canada_source).move_to_element(canada_destination).release().perform() #it does the same thing no conflic but choose one is enough


# Wait for user input before closing the browser window  // will remain open until the user presses the Enter key in the terminal
# input("Press Enter to close the browser...")
time.sleep(5)
driver.quit()

