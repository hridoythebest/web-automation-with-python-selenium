from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www2.hm.com/en_in/divided/shop-by-product/shoes.html")

driver.find_element_by_xpath("""//*[@id="onetrust-accept-btn-handler"]""").click()
driver.find_element_by_xpath("""//*[@id="page-content"]/div/div[2]/ul/li/article/div[1]/a/img""").click()


# name = driver.find_element(By.XPATH, """//*[@id="page-content"]/div/div[2]/ul/li/article/div[2]/h3/a""")
# print(name.text)  # Use .text to get the text content of the element



time.sleep(15)

# Optionally, you can close the browser after the delay
driver.quit()
