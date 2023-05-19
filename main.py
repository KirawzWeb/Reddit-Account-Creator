num_accounts = 5 #Setting account Here

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
from pystyle import *
import time
import random
import string
import requests

os.system('title 0xRedditFucker ^| By KynZay#4521 ^| using : Reddit Creator')

print(Colors.green + "         [" + Colors.gray + "+" + Colors.green + "]" + Colors.gray + " starting up..")
driver = webdriver.Chrome(ChromeDriverManager().install())


for _ in range(num_accounts):
    email = "".join(random.choices(string.ascii_letters + string.digits, k=8)) + "@gmail.com"
    password = "0xBotterEveryware"
    usr = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    print(Colors.green + "         [" + Colors.gray + "+" + Colors.green + "]" + Colors.gray + " loaded !")

    driver.get("https://www.reddit.com/register/")
    time.sleep(5)
    driver.find_element(By.ID, "regEmail").clear()
    time.sleep(0.5)
    driver.find_element(By.ID, "regEmail").send_keys(email)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[3]/button").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[@id='regUsername']").clear() 
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[@id='regUsername']").send_keys(usr)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[@id='regPassword']").clear()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//*[@id='regPassword']").send_keys(password)
    print(Colors.red + "PLEASE RESOLVE CAPTCHA !!")
    time.sleep(25) #you can change this depending on the captcha
    driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div[3]/button").click()

    with open("Created.txt", "a") as f:
        f.write(f'{email}:{password}:{usr}\n')

