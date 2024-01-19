from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/hotels/hotel-listing/?checkin=01212024&city=CTGOI&checkout=01222024&roomStayQualifier=2e0e&locusId=CTGOI&country=IN&locusType=city&searchText=Goa&regionNearByExp=3&rsc=1e2e0e")

print(driver.execute_script("return document.body.scrollHeight"))

# driver.execute_script("window.scrollTo(0, 2000)")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

time.sleep(15)

# Optionally, you can close the browser after the delay
driver.quit()
