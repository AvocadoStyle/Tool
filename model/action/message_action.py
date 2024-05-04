import time

from selenium.common import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from model.Utilities.operation_utils import sleep_decorator
from model.action.browser_action import BrowserAction
from model.action.operation_action import OperationAction


class Message(OperationAction):
    def __init__(self, browser_driver, browser_action):
        super().__init__(browser_driver=browser_driver, browser_action=browser_action)
        self.MAX_COLUMN = 4
        self.MAX_ROW = 4

    @sleep_decorator(prefix_duration=2, postfix_duration=2)
    def press_on_liked_profile(self, row=1, col=1):  # TODO: copy it to `browser_action` BrowserAction class maybe
        """
        Inside The previous likes you can press on profiles, There are 4 profiles per row. We'll use MAX row qty and
        MAX column qty to verify the user didn't insert higher value.
        The row and column will start from `1` which means it's the first profile.
        """
        try:
            if row > self.MAX_ROW or col > self.MAX_COLUMN:
                raise ValueError(f"The row: {row} and column: {col} are outofbounds")
            search = WebDriverWait(self.browser_driver.driver, 50).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"/html/body/div[1]/main/div/div[2]/div/main/div/div/div/div[2]/div[{row}]/div[{col}]"))
            )
            search.click()
            print(f"[debug] pressed on Liked profile")
        except Exception as e:
            error_msg = "Cannot press on the profile inside Likes -> You Like"
            print(f"[error] {error_msg}")
            raise Exception(f"{error_msg}, {e}")

    @sleep_decorator(prefix_duration=2, postfix_duration=2)
    def press_message_button(self):
        """
        Inside the profile Press the message button
        :exception: Not found the MESSAGE button
        """
        try:
            search4 = WebDriverWait(self.browser_driver.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[3]/div/button[2]/div")))
            search4.click()
            print(f"[debug] pressed on message button")
        except Exception as e:
            error_msg = f"Cannot press on the first profile! In the 'You Like' section."
            print(f"[error] {error_msg}")
            raise Exception(f"{error_msg}, {e}")
    @sleep_decorator(prefix_duration=2, postfix_duration=2)
    def press_pass_button(self):
        """
        Will press the pass button and skip the profile immediately
        :exception: Not found the PASS button
        """
        try:
            search4 = WebDriverWait(self.browser_driver.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[3]/div/button[1]/div")))
            search4.click()
            print(f"[deubg] Pressed on the pass button to pass the profile, Will direct to the `You Like` section")
        except Exception as e:
            error_msg = f"Cannot press on the first profile! In the 'You Like' section."
            print(f"[error] {error_msg}")
            raise Exception(f"{error_msg}, {e}")

    @sleep_decorator(prefix_duration=2, postfix_duration=2)
    def press_exit_from_message_text_area(self):
        try:
            print(f"[debug] try to press `X` exit from the message text box with XPath x1")
            search = WebDriverWait(self.browser_driver.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")))
            search.click()
        except Exception as e:
            print(f"[debug] try to press `X` exit from the message text box with XPath x2")
            try:
                search = WebDriverWait(self.browser_driver.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH,
                         "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/button")))
                search.click()
            except Exception as e:
                error_msg = f"Cannot press on the X button and exit the message text area box"
                print(f"[error] {error_msg}")
                raise Exception(f"{error_msg}, {e}")

    def insert_message_content_into_textarea(self, msg_to_send: str):
        """
        Inside the Message Box Will Send a message
        :exception: Raise exception when we've already sent a message, or the message box of the other user is full
         or other disturb.
        """
        try:
            search5 = WebDriverWait(self.browser_driver.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/textarea")))
            time.sleep(1)
            search5.send_keys(msg_to_send)
            time.sleep(2)
            print(f"[debug] sent keys into the text area {msg_to_send}")
        # if their message box is full or already sent msg or other disturb
        except Exception as e:
            error_msg = f"Seems like the message box is full or already sent a msg or other disturb"
            print(f"[error] {error_msg}")
            raise Exception(f"{error_msg}, {e}")

    def send_message(self):
        """
        After the content inserted to the textarea will press the button and send the message
        """
        try:
            search = WebDriverWait(self.browser_driver.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/button")))
            search.click()
            print(f"[debug] inside the message box that opened, "
                  f"pressed Send Message button to send the content inside the text area")
        except Exception as e:
            error_msg = f"Cannot send the message."
            print(f"[error] {error_msg}")
            raise Exception(f"{error_msg}, {e}")


    @sleep_decorator(prefix_duration=1, postfix_duration=1)
    def message(self, msg_to_send: str):
        """
        Message From the people that have been liked in the past. 
        """
        try:
            # start with refresh
            self.browser_driver.driver_refresh()
            # navigate to the main discover page
            self.browser_action.goto_discover_swipe_section()
            # navigate to Likes -> You Like section
            self.browser_action.goto_you_like_section()
            # press on the first profile that appears with column 0 and row 0 by default
            time.sleep(5)
            try:
                print(f"[info] try to press on liked profile x1")
                self.press_on_liked_profile()
            except Exception as e:
                print(f"[info] try to press on liked profile x2")
                self.press_on_liked_profile()
            # press on message button box
            self.press_message_button()
            # try to send message content keys
            try:
                self.insert_message_content_into_textarea(msg_to_send=msg_to_send)
                self.send_message()
                self.press_exit_from_message_text_area()
            except Exception as e:
                # Exception occur, will pass the profile
                self.press_exit_from_message_text_area()
                # self.press_pass_button() # TODO: pass profile only if the inbox of the user is full with '⚠️' sign.
                self.browser_driver.driver_refresh()
                return False
            self.browser_action.goto_you_like_section()
            self.browser_driver.driver_refresh()
            return True

        except Exception as e:
            raise Exception(f"Exception occur {e}")

    def message_quantity(self, quantity):
        print(f"----------------------- start message: quantity={quantity} -----------------------")
        for count in range(quantity):
            self.message()
            print(f"message count={count+1}")