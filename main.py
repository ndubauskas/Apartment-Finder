import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",value=True)
driver = webdriver.Chrome(options=chrome_options)


forms_url = "https://forms.gle/xp2XxuYCTi37bRxb7"
#Excel sheet url: https://docs.google.com/spreadsheets/d/1jNhZBAJ8oboMXx-6cZc2IneEjqK8ojmcFbnKi9YAkD4/edit?resourcekey#gid=1604589917
apartments_url="https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(apartments_url)
web_text = response.text

soup = BeautifulSoup(web_text,"html.parser")

apartments = []
links = []
prices = []
addresses = []
for apartment in soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper"):
    link = apartment.find("a",class_="StyledPropertyCardDataArea-anchor")["href"]
    price = apartment.find("span", class_="PropertyCardWrapper__StyledPriceLine").text.strip()
    address = apartment.find("address", {"data-test": "property-card-addr"}).text.strip()
    links.append(link)
    prices.append(price)
    addresses.append(address)

print(links)
print(prices)
print(addresses)

driver.get(forms_url)

for i in range(0,len(addresses)):
    address_field = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.click()
    address_field.send_keys(addresses[i], Keys.ENTER)

    price_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.click()
    price_field.send_keys(prices[i], Keys.ENTER)

    link_field = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.click()
    link_field.send_keys(links[i], Keys.ENTER)

    submit_button = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    another_request_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

driver.quit()