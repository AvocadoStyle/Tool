import time
from abc import ABC

from selenium.common import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from model.Utilities.operation_utils import sleep_decorator
from model.action.browser_action import BrowserAction
from model.driver.browser_driver import BrowserDriver


class OperationAction(ABC):
    def __init__(self, browser_driver: BrowserDriver, browser_action: BrowserAction):
        self.browser_driver = browser_driver
        self.browser_action = browser_action
