from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# Set up the browser
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# Open a website
driver.get("https://www.google.com")

# Find an element (e.g., the search box)
search_box = driver.find_element(By.NAME, "q")

# Type something into it
search_box.send_keys("Hello, world!")

# Submit the search
search_box.submit()

# Done! Close the browser after a few seconds
import time

time.sleep(5)
driver.quit()
