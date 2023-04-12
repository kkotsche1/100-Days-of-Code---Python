from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")
date_list = []
event_list =[]
event_dictionary = {}
for i in range(1,6):
    widget = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]')
    date = widget.find_element_by_tag_name("time").get_attribute("datetime")
    dates = date.split("T")
    name = widget.find_element_by_tag_name("a").text
    date_list.append(dates[0])
    event_list.append(name)

i=0
while i < len(date_list):
    event_dictionary[i] = {"Name": event_list[i], "Date": date_list[i]}
    i +=1

print(event_dictionary)
