from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()
file_path = r"E:\testing\coding files\PycharmProjects\my first python with HatemQcart\hfiles\siteTabsExample.html" #links open in new window
# file_path = r"E:\testing\coding files\PycharmProjects\my first python with HatemQcart\hfiles\windowsExample.html" #open in the same window


# driver.get("https://www.msn.com")
driver.get("file:///" + file_path.replace("\\", "/"))

print(driver.current_window_handle)
driver.find_element(By.ID, "link2").click() #another tab with its unique id
print(driver.window_handles)
#Loops and if
usa_parentTab = driver.current_window_handle
usa_allTabsLeft = driver.window_handles
for windowX in usa_allTabsLeft:
    print("in the loop tab title before switch:", driver.title)
    # if windowX.casefold() != usa_parentTab.casefold(): #less capable of fetching titles by my own exp
    if windowX != usa_parentTab: #if the new tab/website is different than the first one then do these 2 things
        driver.switch_to.window(windowX)
        print("title after switch", {driver.title}) #system somtimes miss to fetch the title data!
        print("number of tabs is:", len(usa_allTabsLeft)) #just idea in my mind
        time.sleep(1) #1.wait 1sec / 2.then close it
        driver.close() #we only close current tab and have the other one opened still.
        driver.switch_to.window(usa_parentTab) #back again to the first tab "parent"
        print("last window title we current on:",{driver.title})

driver.find_element(By.ID, "link4").click()
time.sleep(1.5)
driver.close() #surprise it closed the parent not link4 here?

time.sleep(5)
# driver.quit()