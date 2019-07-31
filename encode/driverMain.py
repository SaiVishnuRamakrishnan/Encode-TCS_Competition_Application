import registration
import json
import hotelBooking
import flightBooking
import carBooking
import login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def Core():
    driver = webdriver.Chrome()
    return driver

a = []

def store(a):
    data={}
    if(len(a)==5):
        data['result'] = a
        with open('result.json','w') as outfile:
            json.dump(data,outfile)

if __name__ == "__main__":
            driver = Core()
            registration_result = registration.registrationClass().registrationForm(driver)
            a.append(registration_result) 
            hotel_result = hotelBooking.hotelClass().hotelForm(driver)
            a.append(hotel_result)  
            flight_result = flightBooking.flightClass().flightForm(driver)
            a.append(flight_result)  
            car_book_result = carBooking.carClass().carForm(driver)
            a.append(car_book_result)  
            login_result = login.loginClass().login(driver)
            store(a)
            
