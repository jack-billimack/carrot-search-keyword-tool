# Below code installs all Python packages used in this file.
# Selenium is a headless browser that loads a Chrome-based browser(webdriver).
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# This sets up the Chromium webdriver we will use.
# If configured correctly, a blank Chrome browser will pop-up.
driver = webdriver.Chrome()

# This is an input prompt where you tell the code what keyword to look up.
# Note that you can enter multiple words separated by a comma.
print('\n PLEASE ENTER KEYWORD PHRASE \n')
keyword = input() 

# This creates a blank list which will store related keywords to include.
# Note the terminal will print the keywords found on page, but this list is useful for exporting when Python skills advance.
carrot_list = []

# This is the Carrot Tool URL which we will enter into the browser.
carrot_url = 'https://search.carrot2.org/#/web'
# This action, called a "method", will  
driver.get(carrot_url)
wait = WebDriverWait(driver, 100)

# The code below enters the term we want into the browser and searches the Carrot Tool.
search = driver.find_element_by_css_selector(".bp3-input")
search.send_keys(keyword)
search.send_keys(Keys.TAB)
search.send_keys(Keys.ENTER)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'TopCluster')))

# The code below uses a Python "For-Loop" to iterate over the keyword results and print them back to us.
table = driver.find_element_by_css_selector(".ClusterList")

for row in table.find_elements_by_css_selector(".TopCluster"):
    kwd = [td.text for td in row.find_elements_by_css_selector(".labels")]
    print(kwd)
    carrot_list.append(kwd)