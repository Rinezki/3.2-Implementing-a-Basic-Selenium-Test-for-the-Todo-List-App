from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Avaa sovellus paikallisen palvelimen kautta
driver.get("file:///./todo-list/todo-list-app/index.html")

wait = WebDriverWait(driver, 10)

# --------------------
# Lisää regular task
# --------------------
task_input = wait.until(EC.presence_of_element_located((By.ID, "taskInput")))
add_button = wait.until(EC.element_to_be_clickable((By.ID, "addButton")))

task_input.send_keys("Buy groceries")
add_button.click()

# Varmista, että tehtävä lisättiin
tasks = driver.find_elements(By.CSS_SELECTOR, "#taskList li")
print("Regular tasks:", [t.text for t in tasks])

# --------------------
# Lisää important task
# --------------------
important_input = wait.until(EC.presence_of_element_located((By.ID, "importantTaskInput")))
important_add_button = wait.until(EC.element_to_be_clickable((By.ID, "addImportantButton")))

important_input.send_keys("Pay bills")
important_add_button.click()

important_tasks = driver.find_elements(By.CSS_SELECTOR, "#importantTaskList li")
print("Important tasks:", [t.text for t in important_tasks])

time.sleep(2)
driver.quit()