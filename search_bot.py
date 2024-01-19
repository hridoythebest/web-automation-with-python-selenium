from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.google.com")

user_input = driver.find_element_by_xpath("""//*[@id="APjFqb"]""")
user_input.send_keys("mycyberbase")
driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]""").click()
driver.find_element_by_xpath("""//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/div/span/a/h3""").click()



time.sleep(15)

# Optionally, you can close the browser after the delay
driver.quit()
