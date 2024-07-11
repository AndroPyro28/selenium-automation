# from selenium import webdriver
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# # PATH = "C:\Program Files (x86)\chromedriver.exe"

# # driver = webdriver.Chrome(PATH)

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://youtube.com")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time    
from selenium.webdriver.common.action_chains import ActionChains
def launchBrowser():
    
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    driver.maximize_window()
    
    try:
        selectLang = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
        selectLang.click()
    except NameError:
        print(f"error {NameError}")
        driver.quit()

    #* actionChains can do sequence of action simultaneously
    
    big_cookie = driver.find_element(By.ID,"bigCookie")
    # cookie_count = driver.find_element(By.ID,"cookies")
    #* getting all the production price upgrade
    # items=[driver.find_element(By.ID, "productPrice"+ str(i)) for i in range(1,-1,-1)]
    
    actions = ActionChains(driver)
    
    for i in range(5000):
        actions.click(big_cookie)
        actions.perform()
    
    while True:
        pass
    
launchBrowser()