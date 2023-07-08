import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def BudgetFlight( destination: str, min_days: int, max_days: int):

    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)

    driver.get("https://www.azair.eu/")

#START STATION
    default_start_station = " "
    start_station = driver.find_element(By.CSS_SELECTOR, 'input[name=srcAirport]')
    start_station.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, default_start_station, Keys.ENTER)

#DESTINATION
    if destination == '' or 'Anywhere':
        destination = 'Anywhere'

    destination_station = driver.find_element(By.CSS_SELECTOR, 'input[name=dstAirport]')
    destination_station.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, destination, Keys.ENTER)

#DAYS
    if min_days == 0:
        min_days = 3

    minimum_days = driver.find_element(By.CSS_SELECTOR, 'input[name=minDaysStay]')
    minimum_days.send_keys(Keys.BACKSPACE, min_days, Keys.ENTER)

    if max_days == 0:
        max_days = 8

    maximum_days = driver.find_element(By.CSS_SELECTOR, 'input[name=maxDaysStay]')
    maximum_days.send_keys(Keys.BACKSPACE, max_days, Keys.ENTER)

#TRAVELLERS
    default_number_of_travellers = 4
    select_travellers = driver.find_element(By.CSS_SELECTOR, 'select[name=adults]')
    select_travellers.send_keys(default_number_of_travellers)

#PRICES IN PLN
    default_value = "PLN"
    select_value = driver.find_element(By.CSS_SELECTOR, 'select[name=currency]')
    select_value.send_keys(default_value)

#SEARCH
    Search_Button = driver.find_element(By.CSS_SELECTOR, 'input[type=submit]')
    Search_Button.click()

#DIRECT FLIGHTS
    max_changes = 0
    direct_flight = driver.find_element(By.CSS_SELECTOR, 'input[name=maxChng]')
    direct_flight.send_keys(Keys.BACKSPACE, max_changes, Keys.ENTER)

#SEARCH AGAIN
    Search_Button_Again = driver.find_element(By.CSS_SELECTOR, 'input[type=submit]')
    Search_Button_Again.click()
    time.sleep(2)

#MAXIMUM PRICE
    total_price = driver.find_elements(By.CSS_SELECTOR, 'span[class=tp]')
    prices = []
    counter = 0

    for element in total_price:
        price_text = element.text.replace(' zł', '')
        price = int(price_text)
        if price < 300:
            prices.append(element.text)
            counter += 1

#STATION'S NAMES
    start_station_name = driver.find_elements(By.CSS_SELECTOR, 'span[class=from]')
    start_list = []

    for element in start_station_name[:4*counter]:
        start_list.append(element.text)

    new_list = []

    for index in range(len(start_list)):
        if index % 2 == 0 or start_list[index] != '':
            new_list.append(start_list[index].split(' ', 1)[1])

    another_list = []

    for i in range(0, len(new_list), 2):
        new_element = new_list[i] + " - " + new_list[i + 1]
        another_list.append(new_element)

#LINKS
    links = []
    bookmark_div = driver.find_elements(By.CLASS_NAME, 'bookmark')
    for element in bookmark_div[0:counter]:
        link = element.find_element(By.TAG_NAME, "a")
        final_link = link.get_attribute("href")
        links.append(final_link)

    completed_list = [(x, y, z) for x, y, z in zip(another_list, prices, links)]

    driver.quit()

    return completed_list
