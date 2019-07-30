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
                time.sleep(8)
                print("next module")
                # elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/a/strong')
                # elem.click()
                # elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/ul/li[8]/a')
                # elem.click()
                time.sleep(5)

                elem=driver.find_element_by_xpath("//a[contains(.,'Search by Hotel or City Name')]")
                elem.click()
                elem.send_keys('Chennai')
                time.sleep(6)
                elem.send_keys(Keys.RETURN)
                elem=driver.find_element_by_xpath("//input[@name='checkin']")
                elem.click()
                # elem=driver.find_element_by_xpath('/html/body/div[13]/div[1]/table/thead/tr[1]/th[2]')
                # mnth=elem.text
                # time.sleep(4)
                depdat=driver.find_element_by_xpath("//*[@id='dpd1']/div/input")
                depdat.click()
                depdat.clear()
                depdat.send_keys("05/11/2019")


                # elem=driver.find_element_by_xpath('/html/body/div[13]/div[1]/table/thead/tr[1]/th[2]')
                # mnth=elem.text
                # while(1):
                #     if mnth==smonth:
                #         time.sleep(1)
                #         elem=driver.find_element_by_xpath('/html/body/div[13]/div[1]/table/tbody/tr[1]/td[1]')
                #         ssate=elem.text
                #         elem.click()
                #         f = 0
                #         for i in range (1,7):
                #             for j in range (1,8):
                #                 if sdate == int(ssate):
                #                     elem.click()
                #                     f = 1
                #                     break
                #                 else:
                #                     elem=driver.find_element_by_xpath('/html/body/div[13]/div[1]/table/tbody/tr['+str(i)+']/td['+str(j)+']')
                #                     ssate=elem.text
                #             if f == 1:
                #                 break
                #         break
                #     else:
                #         elem=driver.find_element_by_xpath('/html/body/div[13]/div[1]/table/thead/tr[1]/th[3]')#arrow
                #         elem.click()
                #         elem=driver.find_element_by_xpath('/html/body/div[13]/div[1]/table/thead/tr[1]/th[2]')#mounth
                #         mnth=elem.text
                #         time.sleep(1)

                elem=driver.find_element_by_xpath('//*[@id="dpd2"]/div/input')
                elem.click()
                elem.clear()
                elem.send_keys('07/11/2019')

                # elem=driver.find_element_by_xpath('/html/body/div[14]/div[1]/table/thead/tr[1]/th[2]')
                # dmnth=elem.text
                # print(dmnth)
                # while(1):
                #     if dmnth==dmonth:
                #         time.sleep(1)
                #         elem=driver.find_element_by_xpath('/html/body/div[14]/div[1]/table/tbody/tr[1]/td[1]')
                #         dsate=elem.text
                #         elem.click()
                #         f = 0
                #         for i in range (1,7):
                #             for j in range (1,8):
                #                 if ddate == int(dsate):
                #                     elem.click()
                #                     f = 1
                #                     break
                #                 else:
                #                     elem=driver.find_element_by_xpath('/html/body/div[14]/div[1]/table/tbody/tr['+str(i)+']/td['+str(j)+']')
                #                     dsate=elem.text
                #             if f == 1:
                #                 break
                #         break
                #     else:
                #         elem=driver.find_element_by_xpath('/html/body/div[14]/div[1]/table/thead/tr[1]/th[3]')#arrow//
                #         elem.click()
                #         elem=driver.find_element_by_xpath('/html/body/div[14]/div[1]/table/thead/tr[1]/th[2]')#mounth
                #         dmnth=elem.text
                #         time.sleep(1)
                
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

                elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/a/strong')
                elem.click()
                elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/ul/li[8]/a')
                elem.click()
                time.sleep(8)

                elem=driver.find_element_by_xpath('//*[@id="collapse1"]/div[1]/div[3]/label/div/ins')
                elem.click()
                time.sleep(10)
                driver.execute_script("window.scrollTo(0, 10)")

                elem.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[3]/div/table/tbody/tr[1]/td/div[2]/div/h4/a/b')
                elem.click()
                time.sleep(10)

                im = ImageGrab.grab()
                number = random.randrange(1,10000,1)
                im.save('screenshot'+str(number)+'.png')
                time.sleep(3)

                elem=driver.find_element_by_xpath('//*[@id="listing"]/tbody/tr[1]/td/div[3]/form/button')
                elem.click()
                time.sleep(6)
                
                im = ImageGrab.grab()
                number = random.randrange(1,10000,1)
                im.save('screenshot'+str(number)+'.png')
                time.sleep(10)

                driver.execute_script("window.scrollTo(0, 1050)")

                elem=driver.find_element_by_xpath('//*[@id="rooms"]/div[3]/div/div[3]/div/div/div/div[3]/form/button')
                elem.click()

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
                time.sleep(5)

                #report not generated
                im = ImageGrab.grab()
                number = random.randrange(1,10000,1)
                im.save('screenshot'+str(number)+'.png')

                return 1

            except :
                # print(e)
                return 0

if __name__ == "__main__":
    obj = hotelClass()
    obj.hotelForm(driverMain.Core)
    # print(result)
    # driverMain.store(result)


