from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
first_name.send_keys("Konstantin")
last_name.send_keys("Kotschenreuther")
email.send_keys("kotschi123@gmail.com")

submit_button = driver.find_element_by_xpath('/html/body/form/button')
submit_button.click()
sleep(5)