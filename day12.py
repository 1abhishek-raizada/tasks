from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

service = Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.get("https://www.amazon.in/")

search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/div/input")
search_button=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.send_keys("Apple phones")
search_button.click()
time.sleep(5)

#//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]
product_class='//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]'
#next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[29]/div/div/span/ul/li[4]/span/a')

products=[]
for i in range(5):
    print('scraping page:',i+1)
    product=driver.find_elements(By.XPATH,'//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]')
    for value in product:
        products.append(value.text)
    
    time.sleep(2)
    next_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator"]')
   
    next_button.click()
    print('scraped')
    time.sleep(2)

print(products)
with open('phone.csv','w') as cfile:
    writer=csv.writer(cfile)
    for x in products:
        writer.writerow([x])

driver.back()