from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import ElementClickInterceptedException, NoSuchElementException, TimeoutException


class BrowserAction:
    def __init__(self, browser_driver):
        self.browser_driver = browser_driver

    def goto_discover_swipe_section(self, break_condition=False):
        """
        Will go to the Main Page (Where the New Profiles Likes or Dislikes resides).
        :exception TimeoutException: Will handle the exception by refresh the driver and close the open widgets and will
         try once again the current procedure. The break condition is when we're trying to execute this procedure once
         again and it failes with `TimeoutException` it will
        """
        try:
            search = WebDriverWait(self.browser_driver.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/nav/div/span[1]/a[4]"))
            )
            search.click()
            print(f"[debug] Navigate to discover swipe section")
        except TimeoutException as e:
            print(f"[error] not found the element")
            self.browser_driver.driver_refresh()
            self.browser_driver.driver_close_widgets_escape()
            if not break_condition:
                print(f"[error] will try again to run the procedure")
                self.goto_discover_swipe_section(True)
            print(f"[error] couldn't execute the procedure - somthing bad happened")
        except Exception as e:
            raise Exception(f"unfamiliar exception {e}")

    def goto_likes_section(self):
        """
        Will go to likes Section in the main navbar
        """
        try:
            search = WebDriverWait(self.browser_driver.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/nav/div/span[1]/a[5]"))
            )
            search.click()
        except TimeoutException as e:
            print("[error] not found the element")
            self.browser_driver.driver_refresh()
            self.browser_driver.driver_close_widgets_escape()
            self.goto_discover_swipe_section()
        except Exception as e:
            raise Exception(f"[error] unfamiliar exception {e}")

    def goto_you_like_section(self):
        """
        Inside `Likes` section in the main NAVBAR will direct into `You Like` - The previous likes that the user
        have been like in the past.
        """
        try:
            self.goto_likes_section()
            search = WebDriverWait(self.browser_driver.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div/div[2]/section/div/nav/div/span[3]/a"))
            )
            search.click()
            print(f"[debug] Navigate to `You Like` section")
        except TimeoutException as e:
            print("[error] not found the element")
            self.browser_driver.driver_refresh()
            self.browser_driver.driver_close_widgets_escape()
            self.goto_discover_swipe_section()
        except Exception as e:
            raise Exception(f"[error] unfamiliar exception {e}")