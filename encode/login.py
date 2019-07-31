from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.cElementTree as ET
import pyscreenshot as ImageGrab
import random
import logging
import driverMain

class loginClass:

    global email
    global password


    def login(self ,driver):
        try:
            tree = ET.ElementTree(file="data.xml")
            root = tree.getroot()
            for child in root:
                if child.tag == "items":
                    for i in child:
                        email = (i.get('email'))
                        password = (i.get('password'))

            logging.basicConfig(level=logging.INFO,filename='login_log_test.log',filemode='a',format='%(name)s - %(levelname)s - %(message)s')
            logging.info("-----------LOGOUT------------")
            elem = driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[1]/li[5]/a')
            elem.click()
            time.sleep(5)

            elem = driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a')
            elem.click()
            time.sleep(2)

            elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[2]/a')
            elem.click()
            time.sleep(5)

            logging.info("LOGOUT SUCESSFULLY")

            logging.info("-----------LOGIN------------")

            logging.info("LOGIN CRDENTIALS ENTERED")

            elem = driver.find_element_by_xpath('//*[@id="loginfrm"]/div[1]/div[5]/div/div[1]/input')
            elem.click()
            time.sleep(1)
            elem.send_Keys(email)

            elem = driver.find_element_by_xpath('//*[@id="loginfrm"]/div[1]/div[5]/div/div[2]/input')
            elem.click()
            time.sleep(1)
            elem.send_Keys(password)

            elem = driver.find_element_by_xpath('//*[@id="loginfrm"]/button')
            elem.click()
            time.sleep(8)

            logging.info("LOGIN SUCESSFULLY")

            logging.info("SCREENSHOT TAKEN")

            im=ImageGrab.grab(bbox = None)
            # number = random.randrange(1,10000,1)
            im.save('Screenshots/Relogin.png')
            time.sleep(3)

            logging.info("-----------LOGIN SUCESSFULLY TESTED------------")

            return 1

        except:
            return 0

if __name__ == "__main__":
    obj = loginClass()
    obj.login(driverMain.Core)
