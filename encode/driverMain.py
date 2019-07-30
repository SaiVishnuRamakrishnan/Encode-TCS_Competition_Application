import login
import json
import hotelBooking
# from hotelBooking import hotelClass
# from carBooking import carClass
import flightBooking
import carBooking
# from flightBooking import flightClass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def Core():
    driver = webdriver.Chrome()
    return driver

a = []

def store(a):
    data={}
    if(len(a)==4):
        data['result'] = a
        with open('result.json','w') as outfile:
            json.dump(data,outfile)

if __name__ == "__main__":
            driver = Core()
            login_result = login.loginClass().loginForm(driver)
            a.append(login_result)
            hotel_result = hotelBooking.hotelClass().hotelForm(driver)
            a.append(hotel_result)
            flight_result = flightBooking.flightClass().flightForm(driver)
            a.append(flight_result)
            car_book_result = carBooking.carClass().carForm(driver)
            a.append(car_book_result)
            store(a)
            
# test_case1=Lc.loginForm()
# Hc=hotelClass()
# test_case2=Hc.hotelForm()
# Cc=carClass()
# test_case3=Cc.carForm()
# Fc=flightClass()
# test_case4=Fc.flightForm()
# print(test_case1,test_case2,test_case3,test_case4)
