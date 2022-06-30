import requests
import time
import List
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestPlan(object):
    """
    A :class:~testplan.TestPlan object is the ...

    package
    """
    def __init__(self, url, browser_type):
        self.url = url
        self.browser_type = browser_type

    def selectbrower(self, browser_type: str) -> webdriver:
        """docstring for selectbrower"""
        if browser_type == 'Chrome':
            driver_path = os.popen('which chromedriver').read().strip()
            driver = webdriver.Chrome(driver_path)
        elif browser_type == 'Safari':
            # Only one Safari browser instance can be active at any given time
            driver = webdriver.Safari()
        else:
            driver = webdriver.Firefox()

        return driver

    def createtestcase(self, serialnumber: str):
        """docstring for createtestcase"""

        """
        driver = self.selectbrower(self.browser_type)
        driver.get(self.url)
        time.sleep(5)

        testscope = driver.find_element("name", "SerialNumber")

        testscope.send_keys(serialnumber)
        time.sleep(5)

        testscope.send_keys(Keys.RETURN)

        titles = driver.find_element(By.CLASS_NAME, "c-result-tile__title")

        warranty = driver.find_element(By.XPATH, "//div[@data-bind='html: emptyResultText']")

        driver.refresh()
        """

    def checkclicksharewarranty(self, warranty: str):

        assert warranty != "We couldn't find a product with this serial number. Please double-check the serial number and try again."


