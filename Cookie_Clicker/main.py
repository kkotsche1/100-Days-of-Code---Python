from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


total_cookies = 0
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

game_is_on = True

while game_is_on:
    round_is_on = True

    while round_is_on:
        cursor_cost = driver.find_element_by_id('buyCursor')
        cursor_cost = cursor_cost.find_element_by_tag_name("b").text
        cursor_cost = cursor_cost.split(" ")[2]
        cursor_cost = int(cursor_cost.replace(",", ""))
        grandma_cost = driver.find_element_by_id('buyGrandma')
        grandma_cost = grandma_cost.find_element_by_tag_name("b").text
        grandma_cost = grandma_cost.split(" ")[2]
        grandma_cost = int(grandma_cost.replace(",", ""))
        factory_cost = driver.find_element_by_id('buyFactory')
        factory_cost = factory_cost.find_element_by_tag_name("b").text
        factory_cost = factory_cost.split(" ")[2]
        factory_cost = int(factory_cost.replace(",", ""))
        mine_cost = driver.find_element_by_id('buyMine')
        mine_cost = mine_cost.find_element_by_tag_name("b").text
        mine_cost = mine_cost.split(" ")[2]
        mine_cost = int(mine_cost.replace(",", ""))
        shipment_cost = driver.find_element_by_id('buyShipment')
        shipment_cost = shipment_cost.find_element_by_tag_name("b").text
        shipment_cost = shipment_cost.split(" ")[2]
        shipment_cost = int(shipment_cost.replace(",", ""))
        alchemy_lab_cost = driver.find_element_by_id('buyAlchemy lab')
        alchemy_lab_cost = alchemy_lab_cost.find_element_by_tag_name("b").text
        alchemy_lab_cost = alchemy_lab_cost.split(" ")[3]
        alchemy_lab_cost = int(alchemy_lab_cost.replace(",", ""))
        portal_cost = driver.find_element_by_id('buyPortal')
        portal_cost = portal_cost.find_element_by_tag_name("b").text
        portal_cost = portal_cost.split(" ")[2]
        portal_cost = int(portal_cost.replace(",", ""))
        time_machine_cost = driver.find_element_by_id('buyTime machine')
        time_machine_cost = time_machine_cost.find_element_by_tag_name("b").text
        time_machine_cost = time_machine_cost.split(" ")[3]
        time_machine_cost = int(time_machine_cost.replace(",", ""))

        cookie = driver.find_element_by_id("cookie")
        cursor = driver.find_element_by_id("buyCursor")
        grandma = driver.find_element_by_id("buyGrandma")
        factory = driver.find_element_by_id("buyFactory")
        mine = driver.find_element_by_id("buyMine")
        shipment = driver.find_element_by_id("buyShipment")
        alchemy_lab = driver.find_element_by_id("buyAlchemy lab")
        portal = driver.find_element_by_id("buyPortal")
        time_machine = driver.find_element_by_id("buyTime machine")
        timeout = time.time() + 10

        while time.time()<timeout:
            cookie.click()

        current_cookie_count = driver.find_element_by_id("money").text
        current_cookie_count = int(current_cookie_count.replace(",", ""))



        if current_cookie_count > time_machine_cost:
            time_machine.click()
        elif current_cookie_count > portal_cost:
            portal.click()
        elif current_cookie_count > alchemy_lab_cost:
            alchemy_lab.click()
        elif current_cookie_count > shipment_cost:
            shipment.click()
        elif current_cookie_count > mine_cost:
            mine.click()
        elif current_cookie_count > factory_cost:
            factory.click()
        elif current_cookie_count > grandma_cost:
            grandma.click()
        elif current_cookie_count > cursor_cost:
            cursor.click()

        cursor_cost = None
        grandma_cost= None
        factory_cost = None
        mine_cost = None
        shipment_cost = None
        alchemy_lab_cost = None
        portal_cost = None
        time_machine_cost = None
        time.sleep(2)
        round_is_on = False