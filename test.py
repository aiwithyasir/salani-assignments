from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
path = r'C:\chromedriver-win64\chromedriver.exe'
service = Service(path)
service.start()

driver = webdriver.Chrome(path, options=options)
driver.get("https://coinmarketcap.com/")

rows = driver.find_elements(By.XPATH, '//table[contains(@class, "cmc-table")]//tbody/tr')

for row in rows[1:]:
    cols = row.find_elements(By.TAG_NAME, 'td')
    rank = cols[1].text
    name = cols[2].text
    price = cols[3].text
    hour_change = cols[4].text
    day_change = cols[5].text
    week_change = cols[6].text
    market_cap = cols[7].text
    volume = cols[8].text

    print(f"{rank}")