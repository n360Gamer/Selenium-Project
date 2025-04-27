from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up the browser
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# Open a website
driver.get(
    "https://secure.chase.com/web/auth/dashboard#/dashboard/merchantOffers/offerCategoriesPage?accountId=1034016530"
)


def add_cashback_item(index):
    cash_back_boxes = driver.find_elements(By.CLASS_NAME, "r9jbija")
    cash_back_boxes[index].click()
    time.sleep(2)
    driver.get(
        "https://secure.chase.com/web/auth/dashboard#/dashboard/merchantOffers/offerCategoriesPage?accountId=1034016530"
    )

# Find an element (e.g., the search box)
list_of_adding = driver.find_elements(By.CLASS_NAME, "r9jbija")

number_of_boxes = len(list_of_adding)

for i in range(number_of_boxes):
    list_of_adding = driver.find_elements(By.CLASS_NAME, "r9jbija")
    add_cashback_item(i)
    time.sleep(1)

time.sleep(5)
driver.quit()
