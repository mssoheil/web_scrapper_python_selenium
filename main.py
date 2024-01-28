from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r'/usr/bin/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options, service=service )

driver.get("https://yahoo.com")
trending = driver.find_element(By.CLASS_NAME, "trendingNowTextList")
print(trending.text)
driver.quit()