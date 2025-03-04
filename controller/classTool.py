import time

from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.action.browser_action import BrowserAction
from model.user.credentials import User
from model.driver.browser_driver import BrowserDriver
from model.action.like_action import Like
from model.action.message_action import Message


class OkCupidSelenium:
    def __init__(self, user_name, password, driver_path, url, user_cached_data=None):
        self.browser_driver: BrowserDriver = BrowserDriver(driver_path, url)
        self.browser_action: BrowserAction = BrowserAction(self.browser_driver)
        self.user_credentials: User = User(user_name, password)
        self.like_action: Like = None
        self.message_action: Message = None
        self.initialize_objects(user_cached_data)

    def initialize_objects(self, user_cached_data):
        """
        The main initializer of all the handlers
        """
        # Setup the driver object
        self.browser_driver.setupDriver(user_cached_data=user_cached_data)
        self.like_action = Like(browser_driver=self.browser_driver, browser_action=self.browser_action)
        self.message_action = Message(browser_driver=self.browser_driver, browser_action=self.browser_action)
        print("hey")




















    def login(self, driver):
        search = driver.find_element_by_class_name("c0J0grIjyKY6YuiL9OO7")
        search.click()
        time.sleep(2)
        search = driver.find_element_by_name("username")
        time.sleep(2)
        search.send_keys(self.user_credentials.user_name)
        search = driver.find_element_by_name("password")
        time.sleep(2)
        search.send_keys(self.user_credentials.password)
        time.sleep(2)
        search = driver.find_element_by_class_name("login-actions-button")
        search.click()
        time.sleep(10)

    # def message(self, contain, people, driver=None):
    #     people_main = people
    #     full_profile = 0
    #     disturb = 0
    #     cnt_row = 1
    #     cnt_col = 1
    #     driver = self.browser_driver.driver
    #     while people > 0:
    #         print(f"---- Starting once again ----")
    #         print(f"Sent message to people={people}")
    #         print(f"Send message goal={people_main}")
    #         print(f"disurbed times={disturb}")
    #         print(f"full profiles pass={full_profile}")
    #         print(f"col={cnt_col} row={cnt_row}")
    #         # first of all we'll refresh
    #         self.browser_driver.driver_refresh()
    #         # press on the "Likes" in the menu
    #         try:
    #             search = WebDriverWait(driver, 20).until(
    #                     EC.presence_of_element_located((By.XPATH, "//*[@id=\"nav_ratings\"]"))
    #             )
    #             search.click()
    #         except Exception as e:
    #             self.browser_driver.driver_refresh()
    #             continue
    #         # in the "Likes" press "you like"
    #         try:
    #             self.browser_driver.driver_refresh()
    #             search2 = WebDriverWait(driver, 20).until(
    #                 EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/section/div/nav/div/span[3]/a"))
    #             )
    #             search2.click()
    #             time.sleep(1)
    #             self.browser_driver.driver_refresh()
    #             time.sleep(4)
    #         except Exception as e:
    #             self.browser_driver.driver_refresh()
    #             time.sleep(2)
    #             continue
    #
    #         ##### done refactor until here
    #
    #
    #         # press on the first profile
    #         try:
    #             self.browser_driver.driver_refresh()
    #
    #             time.sleep(3)
    #             search3 = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.XPATH, f"//*[@id=\"userRows-app\"]/div/main/div/div/div/div[2]/div[{cnt_row}]/div[{cnt_col}]/div"))
    #             )
    #             search3.click()
    #             time.sleep(2)
    #             self.browser_driver.driver_refresh()
    #
    #             time.sleep(2)
    #         except Exception as e:
    #             print("Cannot press on the first profile! In the 'You Like' section")
    #             self.browser_driver.driver_refresh()
    #             time.sleep(2)
    #             continue
    #         print("debug2")
    #         time.sleep(3)
    #         # inside the profile press "message" button
    #         try:
    #             time.sleep(1)
    #             search4 = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located(
    #                     (By.XPATH, "/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[3]/div/button[2]/div")))
    #             search4.click()
    #             time.sleep(1)
    #         except Exception as e:
    #             print("Trying to press on the 'message' box but it fails!")
    #             self.browser_driver.driver_refresh()
    #             continue
    #         # inside the message box send items
    #         try:
    #             time.sleep(1)
    #             search5 = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located(
    #             (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/textarea")))
    #             time.sleep(1)
    #             search5.send_keys(contain)
    #             time.sleep(2)
    #         # if their message box is full or already sent msg  other disturb, it pass the profile+exit from the profile
    #         except Exception as e:
    #             try:
    #                 time.sleep(1)
    #                 search5 = WebDriverWait(driver, 5).until(
    #                     EC.presence_of_element_located(
    #                         (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/button/i")))
    #                 time.sleep(2)
    #                 search5.click()
    #                 time.sleep(2)
    #             # it will try to send a message with a different message box
    #             except Exception as e:
    #                 try:
    #                     search5 = WebDriverWait(driver, 5).until(
    #                         EC.presence_of_element_located(
    #                             (By.XPATH,
    #                              "/html/body/div[1]/main/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/textarea")))
    #                     time.sleep(2)
    #                     search5.send_keys(contain)
    #                     search5.send_keys(Keys.RETURN)
    #                     time.sleep(2)
    #                 # message full check
    #                 except TimeoutException as e:
    #                     search5 = WebDriverWait(driver, 5).until(
    #                         EC.presence_of_element_located(
    #                             (By.XPATH,
    #                              "/html/body/div[1]/main/div/div[1]/div[2]/div/div[2]/div[2]/span")))
    #                     # if message full pass the profile
    #                     if '⚠️' in search5.text:
    #                         print("message full, pass profile!")
    #                         try:
    #                             search5 = WebDriverWait(driver, 5).until(
    #                                 EC.presence_of_element_located(
    #                                     (By.XPATH,
    #                                      "/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[3]/div/button[1]")))
    #                             search5.click()
    #                             full_profile += 1
    #                         except Exception as e:
    #                             print("couldn't pass the profile - fucked")
    #                 except Exception as e:
    #                     self.browser_driver.driver_refresh()
    #                     cnt_col = cnt_col-1 if cnt_col >= 4 else cnt_col+1
    #                     disturb += 1
    #                     continue
    #                 # will exit now
    #                 try:
    #                     search5 = WebDriverWait(driver, 5).until(
    #                         EC.presence_of_element_located(
    #                             (By.XPATH,
    #                              "/html/body/div[1]/main/div/div[1]/div[2]/div/div[1]/div/button[2]")))
    #                     search5.click()
    #                     people -= 1
    #                     self.browser_driver.driver_refresh()
    #                     continue
    #                 except Exception as e:
    #                     self.browser_driver.driver_refresh()
    #                     continue
    #
    #             # exit the profile + refresh and continue to the next profile (while loop again)
    #             try:
    #                 # time.sleep(1)
    #                 # search5 = WebDriverWait(driver, 20).until(
    #                 #     EC.presence_of_element_located(
    #                 #         (By.XPATH, "/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[3]/div/button[1]/div")))
    #                 # search5.click()
    #                 # time.sleep(2)
    #                 self.browser_driver.driver_refresh()
    #                 cnt_row = 1 if cnt_row >= 4 else cnt_row + 1 if cnt_col >= 4 else cnt_row
    #                 cnt_col = 1 if cnt_col >= 4 else cnt_col + 1
    #                 # time.sleep(5)
    #                 continue
    #             finally:
    #                 pass
    #         print("debug4")
    #         # press send button after insert the message inside the message box
    #         try:
    #             search6 = WebDriverWait(driver, 20).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/button")))
    #             search6.click()
    #         except Exception as e:
    #             print("we're fucked up.")
    #         # exit from the message box
    #         try:
    #             time.sleep(2)
    #             search6 = WebDriverWait(driver, 20).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/button/i")))
    #             search6.click()
    #         except Exception as e:
    #             print("Can't get out from the message box, Will continue to the next")
    #             continue
    #         time.sleep(5)
    #         # refresh the list
    #         self.browser_driver.driver_refresh()
    #         time.sleep(5)
    #         people -= 1

    def location(self, driver):
        search_location = driver.find_element_by_class_name("cardsummary-location")
        return search_location.text