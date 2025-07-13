from selenium import webdriver

# open browser
driver = webdriver.Firefox()

# fetch url
driver.get("https://www.amazon.in")

# find first matching element
element = driver.find_element("css selector", ".a-image-container")

print(element)

# close current tab
driver.close()

# close browser
driver.quit()