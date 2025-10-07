from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

def test_new_tab_functionality(driver):

    driver.get("https://demoqa.com/browser-windows")

    driver.find_element(By.ID, "tabButton").click()

    time.sleep(2)

    windows = driver.window_handles
    driver.switch_to.window(windows[1])  

    
    heading = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    assert heading.text == "This is a sample page", f"Expected heading text to be 'This is a sample page', but got '{heading.text}'"
    print("✅ New tab opened and verified successfully.")

    driver.switch_to.window(windows[0])
