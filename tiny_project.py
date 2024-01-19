from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.google.com")

user_input = driver.find_element_by_xpath("""//*[@id="APjFqb"]""")
user_input.send_keys("House of Dragon")
user_input.send_keys(Keys.ENTER)

driver.find_element_by_xpath("""//*[@id="kp-wp-tab-overview"]/div[5]/div/div/div/div/div[2]/div[1]/div[1]/div/span/a/div/div/div/cite""").click()

time.sleep(3)

driver.find_element_by_xpath("""//*[@id="page43664-band213498-Video218874"]/div[2]/div[1]/img""").screenshot("C:/Users/hrido/OneDrive/Desktop/chrome/drg.png")
driver.find_element_by_xpath("""//*[@id="becomes-max-on-page-banner"]/div[1]/div/div[2]""").screenshot("C:/Users/hrido/OneDrive/Desktop/chrome/drg2.png")






time.sleep(5)
driver.quit()