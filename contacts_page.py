from selenium.webdriver.common.by import By
from time import sleep


class ContactPage():
    def __init__(self, driver):
        self.driver = driver


    def add_contact_btn(self):
        sleep(1)
        btn = self.driver.find_element(By.ID, "com.android.dialer:id/fab_contacts_add")
        return btn


    def send_text_to_name_edit_text(self, send_text):
        sleep(1)
        et = self.driver.find_element(By.XPATH,
                                      "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText")
        et.send_keys(send_text)


    def send_text_to_phone_edit_text(self, send_text):
        sleep(1)
        et = self.driver.find_element(By.XPATH,
                                      "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText")
        et.send_keys(send_text)


    def bithday_btn(self):
        sleep(1)
        btn = self.driver.find_element(By.ID, "com.android.contacts:id/date_view")
        return btn


    def cancel_birthday_btn(self):
        sleep(1)
        btn = self.driver.find_element(By.ID, "android:id/le_datedia_canclebtn")
        return btn


    def save_contact(self):
        sleep(1)
        btn = self.driver.find_element(By.ID, "com.android.contacts:id/menudone")
        btn.click()
