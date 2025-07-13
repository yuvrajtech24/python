# import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# open browser
chrome_driver = webdriver.Chrome()

# fetch url
chrome_driver.get("https://www.amazon.com")

# Locate elements
search_ele = 0
submit_btn_ele = 0
# try:
#     search_ele = chrome_driver.find_element("id", "twotabsearchtextbox")
    
#     submit_btn_ele = chrome_driver.find_element("id", "nav-search-submit-button")
# except:
#     print("some error")
    
# wait
wait = WebDriverWait(chrome_driver, 60)

search_ele = wait.until(EC.presence_of_element_located(("id", "twotabsearchtextbox")))

submit_btn_ele = wait.until(EC.element_to_be_clickable())

# Perform Actions
search_ele.send_keys("pen drive")
submit_btn_ele.click()

