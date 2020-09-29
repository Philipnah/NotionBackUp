from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from time import sleep
import json


# json file gets opened and saves email and password into variables
with open("settings.json") as json_file:
     data = json.load(json_file)
     for i in data["details"]:
          email = i["email"]
          password = i["password"]



def GetToSendEmail(webDelay):
     with webdriver.Firefox() as driver:
          driver.minimize_window()
          driver.get("https://www.notion.so/")
          
          xpath_value = '/html/body/div[1]/div/div[1]/main/section[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/input'
          sleep(webDelay)
          driver.find_element_by_xpath(xpath_value).send_keys(email)
          xpath_value_button = "/html/body/div[1]/div/div[1]/main/section[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]"
          button = driver.find_element_by_xpath(xpath_value_button)
          ActionChains(driver).click(button).perform()

          driver.maximize_window()


webDelay = 0.5
GetToSendEmail(webDelay)