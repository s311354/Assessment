import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestPlan(object):
    """
    A :class:~testplan.TestPlan object is the ...

    Create the ClickShare warranty's test plan, automate the test cases and create one defect excel file

    """
    def __init__(self, url, browser_type):
        self.url = url
        self.browser_type = browser_type

    def selectbrower(self, browser_type: str) -> webdriver:
        """ select the sepcific brower type for the test scope

        :param browser_type: sepcific browser type
        :type  browser_type:  str

        :return:  the browser type
        :rtype:  webdriver
        """

        if browser_type == 'Chrome':
            driver_path = os.popen('which chromedriver').read().strip()
            driver = webdriver.Chrome(driver_path)
        elif browser_type == 'Safari':
            # Only one Safari browser instance can be active at any given time
            driver = webdriver.Safari()
        else:
            driver = webdriver.Firefox()

        return driver

    def createtestcases(self, serialnumber: str, tolerance: int, results: dict) -> None:
        """ create test scope what serial number of a customer's product are supported to get tested, what warranty information to focus on, what bug types the customer is interested in, annd what areas or features should not ne tested by any means

        :param serialnumber:  serial number of a customer's product are supported to get tested
        :type  serialnumber:  str

        :param tolerance:  tolerance to network latancy
        :type  tolerance:  unsigned int

        :param results:  array with the serialnumber of the array in which to store the warranty results once fetched
        :type  results:  defaultdict(str)
        """
        driver = self.selectbrower(self.browser_type)
        driver.get(self.url)
        testscope = driver.find_element("name", "SerialNumber")

        testscope.send_keys(serialnumber)
        testscope.send_keys(Keys.RETURN)

        # Set tolerance to network Latancy
        time.sleep(tolerance)

        # titles = driver.find_element(By.CLASS_NAME, "c-result-tile__title")
        warranty = driver.find_element(By.XPATH, "//div[@data-bind='html: emptyResultText']")

        if not self.checkclicksharewarranty(serialnumber, warranty=warranty.text):
            results[serialnumber] = warranty.text

        driver.refresh()

    def checkclicksharewarranty(self, serialnumber: str, warranty: str) -> bool:
        """ check ClickShare warranty with serial number

        :param serialnumber:  serial number
        :type  serialnumber:  str

        :param warranty:  warranty results
        :type  warranty:  str

        :return:  Description
        :rtype:  Type
        """
        return False if warranty == "We couldn't find a product with this serial number. Please double-check the serial number and try again." else True
