from contacts_page import ContactPage


class TestAndroid():

    def test_add_contact(self, android_driver):
        contact_page = ContactPage(android_driver)
        contact_page.add_contact_btn().click()
        contact_page.send_text_to_name_edit_text("Iris")
        contact_page.send_text_to_phone_edit_text("+77011111011")
        contact_page.bithday_btn().click()
        contact_page.cancel_birthday_btn().click()
        contact_page.save_contact()

    def test_add_contact_without_name(self, android_driver):
        contact_page = ContactPage(android_driver)
        contact_page.add_contact_btn().click()
        contact_page.send_text_to_phone_edit_text("87011111011")
        contact_page.bithday_btn().click()
        contact_page.cancel_birthday_btn().click()
        contact_page.save_contact()

    def test_add_contact_without_phone(self, android_driver):
        contact_page = ContactPage(android_driver)
        contact_page.add_contact_btn().click()
        contact_page.send_text_to_name_edit_text("John")
        contact_page.bithday_btn().click()
        contact_page.cancel_birthday_btn().click()
        contact_page.save_contact()
