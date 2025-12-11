from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()   # Käynnistää Chrome-selaimen

driver.get("https://google.com")   # Avaa Googlen

print(driver.title)   # Tulostaa välilehden nimen

driver.quit()   # Sulkee selaimen