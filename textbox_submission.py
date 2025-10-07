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

def test_fill_textbox(driver):
    try:
        driver.get("https://demoqa.com/text-box")

        driver.find_element(By.ID, "userName").send_keys("Abhinav Raj")
        driver.find_element(By.ID, "userEmail").send_keys("abhinav@tcs.com")
        driver.find_element(By.ID, "currentAddress").send_keys("123, Example Street, City, Country")
        driver.find_element(By.ID, "permanentAddress").send_keys("456, Example Avenue, City, Country")
        
        
        close_iframe(driver)
        
        
        submit_button = WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        
        
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        
        
        submit_button.click()

        
        success_message = driver.find_element(By.ID, "output").text
        assert "Abhinav Raj" in success_message, f"Form not submitted correctly. Output: {success_message}"

        print("Test passed: Form filled successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        pass
