import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("selenium_debug.log"),
        logging.StreamHandler()
    ]
)

logging.info("Starting Selenium test...")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # open todo list
    driver.get("http://localhost:8000/index.html")
    logging.info("Opened todo list in browser")

    # --------------------
    # Add regular task
    # --------------------
    task_input = wait.until(EC.presence_of_element_located((By.ID, "taskInput")))
    add_button = wait.until(EC.element_to_be_clickable((By.ID, "addButton")))
    task_input.send_keys("Buy groceries")
    add_button.click()
    logging.info("added regular task: buy groceries")



    # --------------------
    # Add important task
    # --------------------
    important_input = wait.until(EC.presence_of_element_located((By.ID, "importantTaskInput")))
    important_add_button = wait.until(EC.element_to_be_clickable((By.ID, "addButton2")))
    important_input.send_keys("Pay bills")
    important_add_button.click()
    logging.info("Added important task: Pay bills")

    important_tasks = driver.find_elements(By.CSS_SELECTOR, "#importantTaskList li")
    logging.info(f"Important tasks:", {[t.text for t in important_tasks]})

except Exception as e:
    logging.error(f"Exception occurred: {e}")
    # ---------------------------
    # 6. Save screenshot on error
    # ---------------------------
    driver.save_screenshot("debug.png")
    logging.info("Saved screenshot as debug.png for debugging")

finally:
    time.sleep(2)
    driver.quit()
    logging.info("Closed browser and finished Selenium test")