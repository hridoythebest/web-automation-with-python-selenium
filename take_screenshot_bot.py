from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?sca_esv=599887976&sxsrf=ACQVn0-RuCvm2_3wmqXBQY0k36TDI5c1QA:1705698309345&q=elephant&tbm=isch&source=lnms&sa=X&ved=2ahUKEwi1_cmureqDAxXbb2wGHUi9B8wQ0pQJegQIDxAB&biw=1303&bih=690&dpr=0.9")


driver.save_screenshot("C:/Users/hrido/OneDrive/Desktop/chrome/ele2.png")


time.sleep(15)

# Optionally, you can close the browser after the delay
driver.quit()
