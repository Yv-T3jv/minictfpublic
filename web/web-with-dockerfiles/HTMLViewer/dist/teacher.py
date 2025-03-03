from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def visit_page(html):
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)

    try:

        driver.get("http://localhost:7050/")
        driver.add_cookie({"name": "flag", "value": "IRS{sample_flag}", "path": "/"})
        driver.get(f"http://localhost:7050/?html={html}")
        print(f"Visited: http://localhost:7050/?html={html}")
        time.sleep(5)

    finally:
        # Close the browser
        driver.quit()