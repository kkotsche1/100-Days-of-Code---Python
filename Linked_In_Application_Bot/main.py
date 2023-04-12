from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


linkedin_email = "k_kotschenreuther@yahoo.de"
linkedin_password = "Konstantin.1"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103644278&keywords=life%20science&location=United%20States")
login_button = driver.find_element_by_class_name("nav__button-secondary")
login_button.click()
time.sleep(2)
user_entry = driver.find_element_by_id("username")
password_entry = driver.find_element_by_id("password")
user_entry.send_keys(linkedin_email)
password_entry.send_keys(linkedin_password)
submit_button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
submit_button.click()
time.sleep(2)

job_list = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul')
job_list = job_list.find_elements_by_tag_name("li")


for job in job_list:
    job.click()
    time.sleep(3)
    apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
    apply_button.click()
    time.sleep(10)
    next_button = driver.find_element_by_xpath('//*[@id="ember767"]')
    next_button.click()
    time.sleep(10)