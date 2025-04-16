from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.common.by import By
import time
import csv

service = Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)



def get_heading():

    head=driver.find_element(By.XPATH,'//h1[@id="topic_page_title"]')
    return head.text
   
    
    
list=[]


driver.get('https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/DTLS/rl_cert.cfm')
matches=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[1]/a")
matches.click()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match1=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[2]/a")
match1.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match2=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[10]/a")
match2.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match3=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[4]/a")
match3.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match4=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[6]/a")
match4.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match5=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[20]/a")
match5.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match6=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[19]/a")
match6.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match7=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[18]/a")
match7.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(4)
driver.back()


match8=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[17]/a")
match8.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match9=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[16]/a")
match9.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match10=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[15]/a")
match10.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match11=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[14]/a")
match11.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match12=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[13]/a")
match12.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

match13=driver.find_element(By.XPATH,"/html/body/div[3]/maxamineignore/div[2]/div[2]/span[2]/div/div[2]/ul/li[12]/a")
match13.click()
get_heading()
list.append(f'{get_heading()}')

time.sleep(5)
driver.back()

print(list)
with open('headings.txt','w') as myfile:
    for x in list:
        myfile.write(x + '\n')


driver.back()
driver.quit()
