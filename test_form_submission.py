from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def close_iframe(driver):
    try:
        iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'google_ads_iframe')]")
        driver.switch_to.frame(iframe) 
        close_button = driver.find_element(By.XPATH, "//button[@class='close']")
        close_button.click() 
        driver.switch_to.default_content()
    except Exception as e:
        print("No iframe or unable to switch to iframe, skipping iframe handling:", e)
        pass 

def test_fill_form(driver):
    try:
        
        driver.get("https://demoqa.com/automation-practice-form")

        driver.find_element(By.ID, "firstName").send_keys("Abhinav")
        driver.find_element(By.ID, "lastName").send_keys("Raj")
        driver.find_element(By.ID, "userEmail").send_keys("abhinav@tcs.com")
        
        close_iframe(driver)
        
        male_radio_button = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.XPATH, "//label[text()='Male']"))
        )
        male_radio_button.click()

        driver.find_element(By.ID, "userNumber").send_keys("9876543210")
    
        
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )

        driver.execute_script("arguments[0].scrollIntoView();", submit_button)

        submit_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
        pass
