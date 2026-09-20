from selenium import webdriver

driver = webdriver.ChromiumEdge()
driver.get("https://www.google.com")

print(driver.title)
driver.quit()