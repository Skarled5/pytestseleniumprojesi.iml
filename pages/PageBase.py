

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageBase: # bütün classlarda kullanıcağımız ortak şeyleri PageClass koyarız
    def __init__(self,driver):
        self.driver = driver

    def webelement_listesinden_string_listesi_ver(self,locator): # kod tekrarını azaltıyor
        elements = self.driver.find_elements(*locator)

        liste = []

        for i in elements:
            liste.append(i.text)

    def wait_element_visibility(self,locater):
        element = WebDriverWait(self.driver,30).until(expected_conditions.visibility_of_element_located(locater))
        return element

    def wait_element_presence(self,locater):
        element = WebDriverWait(self.driver,30).until(expected_conditions.presence_of_element_located(locater))
        return element

    def wait_alert_presence(self):
        WebDriverWait(self.driver,10).until(expected_conditions.alert_is_present()) # alert beklicek