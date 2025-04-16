
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#path='/home/abhishek/.wdm/drivers/chromedriver'
import pandas as pd

service = Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
#driver.get('https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/denovo.cfm')
driver.get('https://www.adamchoi.co.uk/overs/detailed')

all_matches_button=driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches_button.click()

matches=driver.find_elements(By.TAG_NAME,'tr')
date=[]
home_team=[]
score=[]
away_team=[]

### getting an error in the below because we need to wait a bit for the button to be available so 
### im commenting this one and adding the wait code
'''
for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home=match.find_element(By.XPATH,'./td[2]').text
    home_team.append(home)
    print(home)
    home_team.append(match.find_element(By.XPATH,'./td[2]').text)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)
'''
WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))

for match in matches:
    try:
        # Extract the data from the cells
        match_date = match.find_element(By.XPATH, './td[1]').text
        home = match.find_element(By.XPATH, './td[2]').text
        match_score = match.find_element(By.XPATH, './td[3]').text
        away = match.find_element(By.XPATH, './td[4]').text
        
        # Append the data to the lists
        date.append(match_date)
        home_team.append(home)
        score.append(match_score)
        away_team.append(away)
        
        # Optionally, print the data for debugging
        print(f"Date: {match_date}, Home: {home}, Score: {match_score}, Away: {away}")

    except Exception as e:
        print(f"Error processing match row: {e}")
df=pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_team':away_team})
df.to_csv('football.csv',index=False)
print(df)
#driver.quit()