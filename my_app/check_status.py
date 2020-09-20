import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def check_status(first_initial, last_name, county, DOB):
    #options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu') 

    wait = .1 #in sec
    url = "https://www.mvp.sos.ga.gov/"
    
    driver = webdriver.Chrome(executable_path='C:\\Users\\chenv\\git\\hackmit2020\\my_app\\chromedriver.exe') #set up webdriver
    driver.get(url) #go to url
    time.sleep(wait) #gives the webpage some time to load
    driver.find_element_by_id("firstName").send_keys(first_initial) #fill in first initial
    driver.find_element_by_id("lastName").send_keys(last_name) #fill in last name
    Select(driver.find_element_by_id("county")).select_by_visible_text(county) #select county
    driver.find_element_by_id("dob").click() #focus on dob inputbox
    driver.find_element_by_id("dob").send_keys(DOB) #input dob
    driver.find_element_by_id("VALIDBTN").click() #submit form

    time.sleep(wait) #gives the webpage some time to load
    try: #checks if failed to find registration
        driver.find_element_by_id("statuscontent").text
    except NoSuchElementException:
        return False
    else:
        status = driver.find_element_by_id("statuscontent").text #get registration status
        driver.close() #close driver
        return True

