from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r'/usr/bin/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options, service=service )

repo = r"https://github.com/mssoheil"

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
        linkHref = fileLink.get_attribute("href")
        print(linkHref)

        if "File" in ariaLabel:
            driver.get(linkHref)
            sections = driver.find_elements(By.TAG_NAME, "section")
            for section in sections:
                if "file-name-id-wide" in section.get_attribute("aria-labelledby"):
                    print(section.text)

driver.quit()