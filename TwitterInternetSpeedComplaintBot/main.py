from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_USER = "#####"
TWITTER_PASS = "#####"


class InternetSpeedTwitterBot:


    def __init__(self):
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.actual_download = None
        self.actual_upload = None


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        cookie_consent_button = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        cookie_consent_button.click()
        time.sleep(2)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(100)
        self.actual_download = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.actual_upload = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        cookie_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
        cookie_button.click()
        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        login_button.click()
        time.sleep(3)
        user_field = self.driver.find_element_by_tag_name("input")
        user_field.send_keys(TWITTER_USER)
        next_button = self.driver.find_element_by_xpath("//div[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
        next_button.click()
        time.sleep(2)
        pass_field = self.driver.find_element_by_name('password')
        pass_field.send_keys(TWITTER_PASS)
        login_button = self.driver.find_element_by_xpath("//div[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/span/span")
        login_button.click()
        time.sleep(2)
        tweet_entry = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet_entry.send_keys(f"My current internet speed is {self.actual_download} Mbps download, and {self.actual_upload} Mbps upload.")
        submit_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        submit_tweet.click()


Ispeed = InternetSpeedTwitterBot()
Ispeed.get_internet_speed()
Ispeed.tweet_at_provider()