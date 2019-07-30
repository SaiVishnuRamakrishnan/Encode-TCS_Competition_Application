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

class loginClass:
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
    
    #crediantionals

    def loginForm(self, driver):
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
                        # smonth=(i.get('smonth'))
                        # sdate=(i.get('sdate'))
                        # dmonth=(i.get('dmonth'))
                        # ddate=(i.get('ddate'))
                        # adult=(i.get('adult'))
                        child=(i.get('child'))
                        phonenumber=(i.get('phonenumber'))
            # driver = webdriver.Chrome()
            elem=driver.get("https://phptravels.com/demo/")
            driver.maximize_window()
            time.sleep(5)

            try:
                # elem=driver.find_element_by_xpath("//*[@id='onesignal-popover-cancel-button']")
                # elem.click()
                # time.sleep(3)    
                elem=driver.find_element_by_xpath("//*[@id='PopupSignupForm_0']/div[2]/div[1]")
                elem.click()
                time.sleep(2)
            except:
                print("Error")
            
            elem=driver.find_element_by_xpath('/html/body/section[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/small')
            elem.click()
            driver.switch_to_window(driver.window_handles[1])
            driver.implicitly_wait(60)

            elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a')
            elem.click()
            elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[2]/a')
            elem.click()
            elem=driver.find_element_by_xpath('//*[@id="headersignupform"]/div[3]/input')
            elem.click()
            elem.send_keys(username)
            elem=driver.find_element_by_xpath('//*[@id="headersignupform"]/div[4]/input')
            elem.click()
            elem.send_keys(lastname)
            elem=driver.find_element_by_xpath('//*[@id="headersignupform"]/div[5]/input')
            elem.click()
            elem.send_keys(phonenumber)
            elem=driver.find_element_by_xpath('//*[@id="headersignupform"]/div[6]/input')
            elem.click()
            elem.send_keys(email)
            elem=driver.find_element_by_xpath('//*[@id="headersignupform"]/div[7]/input')
            elem.click()
            elem.send_keys(password)
            driver.execute_script("window.scrollTo(0, 500)")
            elem=driver.find_element_by_xpath('//*[@id="headersignupform"]/div[8]/input')
            elem.click()
            elem.send_keys(password)
            
            elem=driver.find_element_by_xpath('//*[@id="headersignupform"]/div[9]/button')
            elem.click()

            time.sleep(7)

            elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[1]/li[1]/a/span')
            elem.click()
            time.sleep(5)

            # elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/a/strong')
            # elem.click()
            # elem=driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/ul/li[2]/ul/li[8]/a')
            # elem.click()
            # time.sleep(5)
            # print("ighi")
            return 1
        except :
            return 0

if __name__ == "__main__":
    obj  = loginClass()
    
    obj.loginForm(driverMain.Core)
   
    # driverMain.store()






        


        
    

