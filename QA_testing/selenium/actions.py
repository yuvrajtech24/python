# imports
from selenium import webdriver

# open browser
driver = webdriver.Firefox()

# get url
driver.get("https://www.amazon.in")

# find and element
search_box_ele = driver.find_element("id", "twotabsearchtextbox")

button_ele = driver.find_element("id", "nav-search-submit-button")

# perform action
search_box_ele.send_keys("shoes")
button_ele.click()

# wait for result
# driver.implicitly_wait()

# close tab


# close browser
