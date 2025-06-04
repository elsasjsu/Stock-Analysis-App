import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


def get_stock_data(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}/history"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Wait longer

    # Handle cookie popup
    try:
        consent = driver.find_element("xpath", '//button[contains(text(), "Accept")]')
        consent.click()
        time.sleep(2)
    except:
        pass

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    
    data_rows = []
    table = soup.find("table")
    if not table:
        return [["No data available"]]

    rows = table.find_all("tr")
    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) >= 6:
            date = cols[0].text
            close_price = cols[4].text
            data_rows.append([date, close_price])
    
    # Debug preview
    for entry in data_rows[:5]:
        print("DEBUG:", entry)

    return data_rows[:10]
