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
    # option.add_argument("start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    driver.get("https://dribbble.com")

    # driver.implicitly_wait(10)
    driver.maximize_window()
    
    
    #* (1) selecting the element and interacting with it
    search = driver.find_element(By.NAME, "q")
    search.click()
    
    search.send_keys("cute dogs and cats")
    search.send_keys(Keys.RETURN)
    
    # driver.implicitly_wait(5)
    
    # selecting the main container
    # main = driver.find_element(By.ID, "main")
    # print(main)
    
    
    #* (2) iterating each elements and accessing the text
    # try:
    
    #* waiting for element to load
    #     main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "main")))
    #     names = main.find_elements(By.CLASS_NAME, "display-name")
        
    #     for name in names:
    #         print(f"usernames: {name.text}")
    # except NameError:
    #     print(f"error {NameError}")
    #     driver.quit()
    
    button = driver.find_element(By.LINK_TEXT, "Animation")
    button.click()
    
    while True:
        pass
    
launchBrowser()