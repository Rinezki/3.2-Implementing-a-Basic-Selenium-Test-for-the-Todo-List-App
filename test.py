from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()   # Käynnistää Chrome-selaimen

driver.get("todo-list-app\3.2-Implementing-a-Basic-Selenium-Test-for-the-Todo-List-App/index.html")   # Avaa Googlen

print(driver.title)   # Tulostaa välilehden nimen

