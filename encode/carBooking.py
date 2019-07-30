from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.cElementTree as ET
import pyscreenshot as ImageGrab
import random
import driverMain


class carClass:
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

            def carForm(self ,driver):
                try:
                    tree = ET.ElementTree(file="data.xml")
                    root= tree.getroot()
                    for child in root:
                        if child.tag == "items":
                            for i in child:
                                username=(i.get('username'))
                                email=(i.get('email'))
                                password=(i.get('password'))
                                lastname=(i.get('lastname'))
                                smonth=(i.get('smonth'))
                                sdate=(i.get('sdate'))
                                dmonth=(i.get('dmonth'))
                                ddate=(i.get('ddate'))
                                adult=(i.get('adult'))
                                child=(i.get('child'))
                                phonenumber=(i.get('phonenumber'))
                                cardnumber=(i.get('cardnumber'))

                    
                    elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[1]/li[4]/a')
                    elem.click()
                    time.sleep(8)

                                                    #Pickup Location
                    pickup=driver.find_element_by_xpath("//*[@id='s2id_carlocations']/a/span[1]")
                    pickup.click()
                    driver.implicitly_wait(60)

                                                    #Manchester-Location        
                    manch=driver.find_element_by_xpath("//*[@id='select2-drop']/ul/li[2]/div")
                    manch.click()
                    driver.implicitly_wait(60)

                                                    #To search for search button
                    clc=driver.find_element_by_xpath("//*[@id='body-section']")
                    clc.click()

                                                                        #Date-Depart 
                    date1=driver.find_element_by_xpath("//*[@id='departcar']")
                    date1.click()
                    date1.clear()
                    date1.send_keys("31/07/2019")
                    driver.implicitly_wait(10)
                                                    #Time-Depart
                    t1=driver.find_element_by_xpath("//*[@id='cars']/form/div[4]/div/select/option[15]")
                    t1.click()
                    driver.implicitly_wait(60)
                                                    #Date-Return
                    date2=driver.find_element_by_xpath("//*[@id='returncar']")
                    date2.click()
                    date2.clear()
                    date2.send_keys("02/08/2019")
                    driver.implicitly_wait(10)                                
                                                    #Time-Return
                    t2=driver.find_element_by_xpath("//*[@id='cars']/form/div[6]/div/select/option[19]")
                    t2.click()
                    driver.implicitly_wait(60)                                 
                                                    #Search     
                    search=driver.find_element_by_xpath("//*[@id='cars']/form/div[7]/button")
                    search.click()
                    driver.implicitly_wait(60)
                                                    #Car-Page
                    kia=driver.find_element_by_xpath("//*[@id='body-section']/div[6]/div/div[3]/div/table/tbody/tr/td/div[2]/div/h4/a/b")                                
                    kia.click()
                                                    #USD to INR 
                    usd=driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[2]/a")
                    usd.click()
                    inr=driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/ul/li[2]/ul/li[8]/a")
                    inr.click()
                    driver.execute_script("window.scrollTo(0, 1000)")
                                                    #Book-Now
                    time.sleep(10)                           
                    bknow=driver.find_element_by_xpath("//*[@id='body-section']/div[4]/div/div[2]/form/button")                                
                    bknow.click()

                    time.sleep(6)
                    #error in filling details

                    im = ImageGrab.grab()
                    number = random.randrange(1,10000,1)
                    im.save('screenshot'+str(number)+'.png')
                    time.sleep(3)

                    driver.execute_script("window.scrollTo(0, 900)")

                    elem=driver.find_element_by_xpath('//*[@id="body-section"]/div/div[1]/div/div[1]/div/div[4]/button')
                    elem.click()
                    time.sleep(8)

                    driver.execute_script("window.scrollTo(0, 50)")

                    im = ImageGrab.grab()
                    number = random.randrange(1,10000,1)
                    im.save('screenshot'+str(number)+'.png')
                    time.sleep(3)

                    driver.execute_script("window.scrollTo(0, 1000)")

                    elem=driver.find_element_by_xpath('//*[@id="downloadInvoice"]')
                    elem.click()
                    time.sleep(5)

                    driver.execute_script("window.scrollTo(0, 1000)")

                    elem=driver.find_element_by_xpath('//*[@id="btn"]')
                    elem.click()
                    time.sleep(4)

                    elem=driver.find_element_by_xpath('//*[@id="body-section"]/div[1]/div[2]/div[2]/center/button[2]')
                    elem.click()

                    elem=driver.find_element_by_xpath('//*[@id="gateway"]/option[5]')
                    elem.click()
                    time.sleep(5)

                    elem=driver.find_element_by_xpath('//*[@id="8"]')
                    elem.click()
                    elem.send_keys(Keys.RETURN)

                    return 1

                except :
                    return 0
if __name__ == "__main__":
    obj = carClass()
    obj.carForm(driverMain.Core)
    # driverMain.store(result)











    