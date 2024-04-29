from controller.classTool import OkCupidSelenium
from dict import *
import time

if __name__ == "__main__":
    like_counter = 0
    dislike_counter = 0
    check_counter = 1000
    # represents locations
    saved_locations = ["`Akko", "Qiryat Yam", "Haifa", "Qiryat Motzkin", "Qiryat Bialik", "`Afula", "Yoqne`am",
                       "Or `Aqiva", "Tiberias", "Shelomi", "Karmi’el", "Ma`alot", "Hadar HaKarmel"]
    driver_path = "chromedriver.exe"
    okcupid_url = "https://www.okcupid.com"
    user_name = T["user_name"]
    password = T["password"]
    # ok = OkCupidSelenium(user_name, password, PATH)
    # contain = "*משחק אותה שלא מתלהב בכלל* מה קורה?"
    # contain = "*משחק אותה שלא מתלהב* מה קורה?"
    contain = "את ממש מוכרת לי"
    people = 50000
    # gets the cache data path of the user, And if there isn't it will retrieve `None`, And it's valid behavior.
    usr_cached_data = T.get('user_cache_data')
    ok = OkCupidSelenium(user_name, password, driver_path, okcupid_url, '')
    people_max_qty_to_msg = 40
    while True:
        ok.message(contain=contain, people=people_max_qty_to_msg)
        # ok.like_action.like_quantity(quantity=10)
        # people_max_qty_to_msg = 10
        time.sleep(2)
