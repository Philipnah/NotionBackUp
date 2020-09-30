from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from time import sleep
import json

# import os.path, time
# print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

# json file gets opened and saves email and password into variables
with open("settings.json") as json_file:
     data = json.load(json_file)
     for i in data["details"]:
          email = i["email"]
          password = i["password"]

def AwaitInput():
     input("Press enter to exit...")


def InsertEnter(xpath_value, payload):
     sleep(webDelay)
     driver.find_element_by_xpath(xpath_value).send_keys(payload)
     driver.find_element_by_xpath(xpath_value).send_keys(Keys.RETURN)


def ClickButton(xpath_value_button):
     button = driver.find_element_by_xpath(xpath_value_button)
     ActionChains(driver).click(button).perform()


def GetToSendEmail(webDelay):
     
     #driver.minimize_window()
     driver.get("https://www.notion.so/login")

     sleep(0.25)
     xpath_value = '/html/body/div[1]/div/div[1]/main/section/div/div/div/div[2]/div[3]/div[3]/input'
     InsertEnter(xpath_value, email)
     
     sleep(0.3)
     xpath_value = "/html/body/div[1]/div/div[1]/main/section/div/div/div/div[2]/div[3]/div[5]/input"
     InsertEnter(xpath_value, password)

     sleep(2.8)
     xpath_value_button = "/html/body/div[1]/div/div[1]/div[1]/div/div/div/div[4]/div[3]/div/div[2]/div"
     ClickButton(xpath_value_button)

     sleep(1)
     xpath_value_button = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[9]/div[2]"
     ClickButton(xpath_value_button)

     sleep(1)
     xpath_value_button = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[12]/div"
     ClickButton(xpath_value_button)

     sleep(1<)
     xpath_value_button = "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div/div[2]/div[2]"
     ClickButton(xpath_value_button)

     AwaitInput()



with webdriver.Firefox() as driver:
     webDelay = 0.5
     GetToSendEmail(webDelay)
     exit()
