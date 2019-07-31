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



class flightClass:
            
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

            def flightForm(self ,driver):
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

                    logging.basicConfig(level=logging.INFO,filename='flight_log_test.log',filemode='a',format='%(name)s - %(levelname)s - %(message)s')
                    logging.info("-----------FLIGHT BOOKING----------")
                    elem = driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[1]/li[2]/a/span')
                    elem.click()
                    time.sleep(5)

                    im=ImageGrab.grab(bbox = None)
                    # number = random.randrange(1,10000,1)
                    im.save('Screenshots/flight_main_page.png')
                    time.sleep(3)

                                        #Checkbox-Oneway
                    logging.info("------------ENTERING USER REQURIMENTS-----------")
                    checkone = driver.find_element_by_xpath("//*[@id='thflights']/div[9]/div[1]/div/div/ins")      
                    checkone.click()
                    driver.implicitly_wait(10) 

                                                            #Enter Country
                    country = driver.find_element_by_xpath("//*[@id='s2id_origin']/a")      
                    country.click() 
                    country.send_keys("Chennai") 
                    time.sleep(5)
                    country.send_keys(Keys.RETURN)

                                                            #Enter Destination
                    dest = driver.find_element_by_xpath("//*[@id='s2id_destination']/a")
                    dest.click()
                    dest.send_keys("Delhi") 
                    time.sleep(3)
                    dest.send_keys(Keys.RETURN) 

                                                            #Date
                    datedep = driver.find_element_by_xpath("//*[@id='departure']")
                    datedep.click()
                    datedep.clear()
                    datedep.send_keys("2019-07-31")
                    driver.implicitly_wait(10)
                                            #Passengers-Popup
                    passen = driver.find_element_by_xpath("//*[@id='thflights']/div[5]/div/input")
                    passen.click()
                    time.sleep(2)
                                            #No. of Adults
                    adult = driver.find_element_by_xpath("//*[@id='madult']/option[1]")
                    adult.click()
          
                                                #done

                    donebutton = driver.find_element_by_xpath("//*[@id='sumManualPassenger']")
                    donebutton.click()       
                    time.sleep(3)                   
                                                #Search                                                     
                    searchflight = driver.find_element_by_xpath("//*[@id='thflights']/div[6]/button")
                    searchflight.click()   
                    time.sleep(4)
                    logging.info("CHANGING CURRENCY")
                                            #USD to INR
                    usd = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[2]/a")
                    usd.click()
                    inr = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[2]/ul/li[8]/a")
                    inr.click()
                    time.sleep(3)

                    logging.info("BOOKING A FLIGHT")
                                            #Book a Flight
                    bookflight = driver.find_element_by_xpath("//*[@id='form_0']/div/button")                        
                    bookflight.click()

                    driver.execute_script("window.scrollTo(0, 700)")

                    elem = driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/a/strong')
                    elem.click()
                    elem = driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/ul/li[8]/a')
                    elem.click()
                    time.sleep(5)

                    elem = driver.find_element_by_xpath('//*[@id="name"]')
                    elem.click()
                    elem.send_keys(username)

                    elem = driver.find_element_by_xpath('//*[@id="surname"]')
                    elem.click()
                    elem.send_keys(lastname)
                    driver.execute_script("window.scrollTo(0, 900)")

                    elem = driver.find_element_by_xpath('//*[@id="email"]')
                    elem.click()
                    elem.send_keys(email)

                    elem = driver.find_element_by_xpath('//*[@id="phone"]')
                    elem.click()
                    elem.send_keys(phonenumber)

                    elem = driver.find_element_by_xpath('//*[@id="birthday"]')
                    elem.click()
                    elem.send_keys('1998-01-01')

                    elem = driver.find_element_by_xpath('//*[@id="cardno"]')
                    elem.click()
                    elem.send_keys(cardnumber)

                    elem = driver.find_element_by_xpath('//*[@id="expiration"]')
                    elem.click()
                    elem.send_keys('2020-01-01')

                    elem = driver.find_element_by_xpath('//*[@id="nationality"]/option[99]')
                    elem.click()


                    driver.execute_script("window.scrollTo(0, 1000)")
                    time.sleep(5)

                    elem = driver.find_element_by_xpath('//*[@id="cardtype"]/option[2]')
                    elem.click()
                    time.sleep(1)

                    elem.find_element_by_xpath('//*[@id="card-number"]')
                    elem.click()
                    elem.send_keys(cardnumber)

                    elem = driver.find_element_by_xpath('')
                    elem.click()
                    time.sleep(1)

                    elem = driver.find_element_by_xpath('//*[@id="expiry-month"]/option[2]')
                    elem.click()
                    time.sleep(1)

                    elem = driver.find_element_by_xpath('//*[@id="cvv"]')
                    elem.click()
                    elem.send_keys('112')

                    logging.info("CRDENTIALS ENTERED")

                    elem = driver.find_element_by_xpath('//*[@id="confirmBooking"]')
                    elem.click()
                    time.sleep(10)

                    logging.error("AVAIBALITY CHECKING")

                    im=ImageGrab.grab(bbox = None)
                    # number = random.randrange(1,10000,1)
                    im.save('Screenshots/flight_booking.png')
                    driver.execute_script("window.scrollTo(0, 0)")

                    logging.info("SCREENSHOT CAPTURED")

                    logging.info("----------FLIGHT BOOKING SUCESSFULLY TESTED-----------")

                    return 1

                except:
                    return 0


if __name__ == "__main__":
    obj = flightClass()
    obj.flightForm(driverMain.Core)
    # driverMain.store(result)











