import time

from selenium.common import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from model.Utilities.operation_utils import sleep_decorator
from model.action.browser_action import BrowserAction


class Message:
    def __init__(self, browser_driver):
        self.browser_driver = browser_driver
        self.browser_action = BrowserAction(self.browser_driver)

    def message(self):
        """
        Message From the people that have been liked in the past. 
        """
        pass


