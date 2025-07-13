from selenium import webdriver

# launch web browser
driver = webdriver.Firefox()

# open a url
driver.get("https://amazon.in")

# close the current tab
driver.close()

# close the browser
driver.quit()