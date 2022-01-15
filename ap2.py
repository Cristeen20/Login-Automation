
from selenium import webdriver
import time
from random import randint

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome('C:\\Users\\HP\\Downloads\\chromedriver.exe')
from selenium.webdriver.common.by import By


def login_link():
    driver.get("https://kaggle.com/")
    time.sleep(randint(2,6))

 
        
    sign=driver.find_element(By.XPATH,'//*[@id="site-container"]/div/div[1]/div[2]/div[2]/div[1]/a/button')
    sign.click()
    time.sleep(randint(2,6))


    em=driver.find_element(By.XPATH,'//*[@id="site-container"]/div[1]/div/form/div[2]/div/div[2]')
    em.click()
    time.sleep(randint(2,6))
    
  
    driver.find_element(By.XPATH,'//*[@id="site-container"]/div[1]/div/form/div[2]/div[1]/div/label/input').send_keys("-enter username-")
    driver.find_element(By.XPATH,'//*[@id="site-container"]/div[1]/div/form/div[2]/div[2]/div/label/input').send_keys("-enter password-")
    time.sleep(randint(2,6))


    sub=driver.find_element(By.XPATH,'//*[@id="site-container"]/div[1]/div/form/div[2]/div[3]/button')
    sub.click()


login_link()