from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'http://adamchoi.co.uk/leagues/spain-la-liga'
path = r'C:\chromedriver-win64\chromedriver.exe'
service = Service(path)
service.start()

driver = webdriver.Chrome(path)
driver.get(website)
driver.find_element_by_xpath("//input[@type='checkbox'][@name='feature_six_browse-bin'][@aria-label='English']")
driver.find_element_by_xpath("//a[@data-ng-click=\"vm.setTabType('Top Players')\"]").click()