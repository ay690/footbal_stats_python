from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/overs/detailed"
path = "D:/Program Files x86/chromedriver-win64/chromedriver-win64/chromedriver.exe"

service = Service(path)

driver = webdriver.Chrome(service=service)

driver.get(website)


# for x-path  go on console and use "ctrl + F"
# x-path syntax //tagName[@AttributeName="Value"]

# loacte the button 
all_matches_button = driver.find_element(By.XPATH, ('//label[@analytics-event="All matches"]'))

# click on the button 
all_matches_button.click()

# extracting data from table

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("Italy")

dropdown2 = Select(driver.find_element(By.ID, "league"))
dropdown2.select_by_visible_text("Serie B")

time.sleep(5)

matches = driver.find_elements(By.TAG_NAME, ("tr"))

date = []
home_team = []
score = []
away_team = []

for match in matches:
    # print(match.text)
    dates = match.find_element(By.XPATH, "./td[1]").text
    date.append(dates)
    # print(dates)
    home_team.append(match.find_element(By.XPATH, "./td[2]").text)
    score.append(match.find_element(By.XPATH, "./td[3]").text)
    away_team.append(match.find_element(By.XPATH, "./td[4]").text)

time.sleep(20)

# make dataframe that is df
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_stats.csv', index=False)
df.to_json('football_stats.json', orient='records')
print(df)


