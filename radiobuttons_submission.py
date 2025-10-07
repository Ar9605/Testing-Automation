from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_radio_buttons_elements_section(driver):
    
    driver.get("https://demoqa.com/radio-button")
    
    yes_radio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='yesRadio']"))
    )
    
    yes_radio_button.click()

  
    assert driver.find_element(By.ID, "yesRadio").is_selected(), "Yes radio button should be selected."
    print("Yes radio button is selected.")

    # Wait for the message to appear after clicking the "Yes" radio button
    yes_message = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".text-success"))
    ).text
    
    print("Message after selecting 'Yes':", yes_message)
    
    assert yes_message == "Yes", f"The message should be 'Yes'. Found: {yes_message}"

    impressive_radio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='impressiveRadio']"))
    )
    
    impressive_radio_button.click()
