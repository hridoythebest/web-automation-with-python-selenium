from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")

time.sleep(5)

driver.find_element_by_xpath("""//*[@id="top-banner"]/div[2]/div""").click()
driver.find_element_by_xpath("""//*[@id="SW"]/div[1]/div[2]/div/div/nav/ul/li[2]/span/a/span[1]/span""").click()

time.sleep(15)

# Optionally, you can close the browser after the delay
driver.quit()
