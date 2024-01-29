from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r'/usr/bin/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options, service=service )

repo = r"https://github.com/usernam121"

repoPage = driver.get(f"{repo}?tab=repositories")
repositoriesWrapper = driver.find_element(By.ID, "user-repositories-list")

repositories = repositoriesWrapper.find_elements(By.TAG_NAME, "li")

for repository in repositories:
    repositoryItem = repository.find_element(By.TAG_NAME, "a")
    repositoryLink = repositoryItem.get_attribute("href")

    repositoryPage = driver.get(repositoryLink)

    repositoryRow = driver.find_elements(By.CLASS_NAME, "react-directory-row")

    for row in repositoryRow:

        nameCell = row.find_element(By.CLASS_NAME, "react-directory-row-name-cell-large-screen")
        fileLink = nameCell.find_element(By.TAG_NAME, "a")
        ariaLabel = fileLink.get_attribute("aria-label")
        href = fileLink.get_attribute("href")

        if "File" in ariaLabel:
            driver.get(href)
            links = driver.find_elements(By.TAG_NAME, "a")
            for link in links:
                if link.text == "Raw":
                    link.click()
                    html = driver.page_source
                    print(html)

driver.quit()