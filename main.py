from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the browser
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

CHASE_URL = os.getenv("CHASE_URL")
index = 0
try:
    while True:
        # Check if the "Add" button is present
        driver.get(CHASE_URL)
        time.sleep(1)  # Wait for the page to load
        wait = WebDriverWait(driver, 5)

        add_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "r9jbijb"))
        )
        add_button.click()
        index += 1
        print(f"Clicked on cashback offer {index}")
        time.sleep(1)

except TimeoutException as e:
    print("No more cashback offers to add.")
    driver.quit()
