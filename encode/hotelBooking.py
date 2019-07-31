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

class hotelClass:

        global username
        global email
        global password
        global lastname
        global smonth
        global sdate 
        global dmonth
        global ddate
        global adult
        global child
        global phonenumber
        global cardnumber

        def hotelForm(self, driver):
            try:
                tree = ET.ElementTree(file = "data.xml")
                root = tree.getroot()
                for child in root:
                    if child.tag == "items":
                        for i in child:
                            username = (i.get('username'))
                            email = (i.get('email'))
                            password = (i.get('password'))
                            lastname = (i.get('lastname'))
                            smonth = (i.get('smonth'))
                            sdate = (i.get('sdate'))
                            dmonth = (i.get('dmonth'))
                            ddate = (i.get('ddate'))
                            adult = (i.get('adult'))
                            child = (i.get('child'))
                            phonenumber = (i.get('phonenumber'))
                            cardnumber = (i.get('cardnumber'))
                
                logging.basicConfig(level=logging.INFO,filename='hotel_log_test.log',filemode='a',format='%(name)s - %(levelname)s - %(message)s')
                logging.info("----------HOTEL BOOKING------------")
                logging.info("ENTERING USER REQUEST CREDENTIALS")

                time.sleep(8)

                im=ImageGrab.grab(bbox = None)
                # number = random.randrange(1,10000,1)
                im.save('Screenshots/hotel_main_page.png')
                time.sleep(3)

                driver.switch_to.window(driver.window_handles[1])

                elem = driver.find_element_by_xpath("//a[contains(.,'Search by Hotel or City Name')]")
                elem.click()
                elem.send_keys('Chennai')
                time.sleep(6)
                elem.send_keys(Keys.RETURN)
                elem=driver.find_element_by_xpath("//input[@name='checkin']")
                elem.click()

                depdat=driver.find_element_by_xpath("//*[@id='dpd1']/div/input")
                depdat.click()
                depdat.clear()
                depdat.send_keys("05/11/2019")

                elem=driver.find_element_by_xpath('//*[@id="dpd2"]/div/input')
                elem.click()
                elem.clear()
                elem.send_keys('07/11/2019')
                
                elem=driver.find_element_by_xpath("//input[contains(@data-toggle,'collapse')]")
                elem.click()
                elem=driver.find_element_by_xpath("//input[contains(@name,'adults')]")
                elem.click()
                elem.clear()
                elem.send_keys(adult)
                elem=driver.find_element_by_xpath("//input[contains(@name,'child')]")
                elem.click()
                elem.clear()
                elem.send_keys(child)
                elem.send_keys(Keys.RETURN)
                time.sleep(6)
                logging.info("USER CREDENTIALAS ENTERED")
                
                logging.info("CHANGING THE CURRENCY")
                elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/a/strong')
                elem.click()
                elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/ul/li[8]/a')
                elem.click()
                time.sleep(10)

                logging.info("APPLYING FILTERS")
                elem=driver.find_element_by_xpath('//*[@id="collapse1"]/div[1]/div[3]/label/div/ins')
                elem.click()
                time.sleep(10)
                driver.execute_script("window.scrollTo(0, 10)")

                elem.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[3]/div/table/tbody/tr[1]/td/div[2]/div/h4/a/b')
                elem.click()
                time.sleep(10)

                logging.error("FILTERS NOT APPLIED")
                logging.info("SCREENSHOT CAPTURED")
                im=ImageGrab.grab(bbox = None)
                # number = random.randrange(1,10000,1)
                im.save('Screenshots/filter_not_applied.png')
                time.sleep(3)
                
                logging.info("SELECTING HOTEL")
                elem=driver.find_element_by_xpath('//*[@id="listing"]/tbody/tr[1]/td/div[3]/form/button')
                elem.click()
                time.sleep(6)
                
                logging.error("NO OTHER THAN DETAILS BUTTON IS USED TO SELECT HOTEL")
                logging.info("SCREENSHOT CAPTURED")
                im=ImageGrab.grab(bbox = None)
                # number = random.randrange(1,10000,1)
                im.save('Screenshots/hotel_select.png')
                time.sleep(10)

                driver.execute_script("window.scrollTo(0, 1050)")

                elem=driver.find_element_by_xpath('//*[@id="rooms"]/div[3]/div/div[3]/div/div/div/div[3]/form/button')
                elem.click()
                
                logging.info("ENTERING USER CREDENTIALS")
                elem=driver.find_element_by_xpath('//*[@id="first_name"]')
                elem.click()
                elem.send_keys(username)

                elem=driver.find_element_by_xpath('//*[@id="last_name"]')
                elem.click()
                elem.send_keys(lastname)

                elem=driver.find_element_by_xpath('//*[@id="email"]')
                elem.send_keys(email)
                

                elem=driver.find_element_by_xpath('//*[@id="country_code"]')
                elem.click()
                elem.send_keys('i')
                elem.send_keys('i')
                elem.send_keys(Keys.RETURN)

                elem=driver.find_element_by_xpath('//*[@id="phone_number"]')
                elem.click()
                elem.send_keys(phonenumber)

                driver.execute_script("window.scrollTo(0, 1000)")
                
                logging.info("ENTERING USER CARD CREDENTIALS")
                elem=driver.find_element_by_xpath('//*[@id="cardHolderName"]')
                elem.click()
                elem.send_keys(username)

                elem=driver.find_element_by_xpath('//*[@id="cardNumber"]')
                elem.click()
                elem.send_keys(cardnumber)

                elem=driver.find_element_by_xpath('//*[@id="thhotels"]/div[2]/form/div[1]/div[2]/div[2]/div[3]/div[1]/div[5]/div[5]/select/option[5]')
                elem.click()

                elem=driver.find_element_by_xpath('//*[@id="cardCVC"]')
                elem.click()
                elem.send_keys('211')

                elem=driver.find_element_by_xpath('//*[@id="completeBooking"]')
                elem.click()
                time.sleep(8)
                
                logging.error("REPORT NOT GENERATED")
                logging.info("SCREEN CAPTURED")
                #report not generated
                im=ImageGrab.grab(bbox = None)
                # number = random.randrange(1,10000,1)
                im.save('Screenshots/hotel_boking.png')

                logging.info("-----------------HOTEL BOOKING SUCESSFULLY TESTED-------------------")
        
                return 1

            except :
                # print(e)
                return 0

if __name__ == "__main__":
    obj = hotelClass()
    obj.hotelForm(driverMain.Core)
 


