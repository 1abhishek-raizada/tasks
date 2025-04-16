from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
x=input('Enter the city name to check weather: ')
j=[]
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://www.accuweather.com/")



search=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[3]/div/div[1]/div[1]/form/input')

search.send_keys(x)
search.send_keys(Keys.ENTER)
#//p[@class="location-name"]
time.sleep(8)
results=driver.find_element(By.XPATH,'//p[@class="location-name"]')
results.click()
loc=driver.find_elements(By.XPATH,'//span[@class="value"]')

for values in loc:
    j.append(values.text)
print(f'Temp: {j[0]},\nWind Direction: {j[1]}, \nWind Speed: {j[2]}, \nAir Quality: {j[3]}')    
#data=[]    
#for keys in j:
#    temp,wind_dir,wind_speed,air_quality=keys.split()
#   
#    k={'temperature':temp,'wind direction':wind_dir,'wind-speed':wind_speed,'air-quality':air_quality}
#    data.append(k)
#print(data)    
time.sleep(3)
