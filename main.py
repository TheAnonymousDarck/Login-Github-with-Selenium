from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.github.com/login")

user = driver.find_element(By.ID, "login_field")
user.send_keys(config('GITHUB_USER'))
time.sleep(5)

password = driver.find_element(By.ID, "password")
password.send_keys(config('GITHUB_PASSWORD'))

user.send_keys(Keys.ENTER)