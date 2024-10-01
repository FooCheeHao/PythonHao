from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import csv

C_Service = webdriver.ChromeService(executable_path="/usr/bin/chromedriver")
driver=webdriver.Chrome(service=C_Service)

# Ask user for the number of pages to scrape
user_input = input("\nPlease enter number total page (Higher page counts will take longer): ")
time.sleep(3)

# Function to scrape titles from a each single page
def scrape_titles_from_page(page_number):
    driver.get(f'https://edition.cnn.com/search?q=&from={page_number}0&size=10&page={page_number}&sort=newest&types=all&section=')
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'container__headline-text')))
    titles = driver.find_elements(By.CLASS_NAME, 'container__headline-text')
    return [title.text for title in titles]

# Function to save titles to a CSV file
def save_titles_to_csv(titles, csv_file):
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([f'\nPage{current_page}: ']) 
        for title in titles:
            writer.writerow([title])

# Setup the CSV file
csv_file = 'cnnnews.csv'
max_pages = int(user_input)
current_page = 1

# Initialize the CSV file with headers
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['======Title Scraping Record======'])
    writer.writerow(['News Titles: '])
# Loop through each page and scrape the titles on terminal
while current_page <= max_pages:
    print(f"Scraping news processing......({current_page}/{user_input})")
    titles = scrape_titles_from_page(current_page)
    save_titles_to_csv(titles, csv_file)
    current_page += 1
    time.sleep(3)

# Print completion message and close the browser
print("\n======================================================")
print("Total page already scraping: ", user_input)
print("CSV record for all pages complete, pls check csv file.")

driver.quit()