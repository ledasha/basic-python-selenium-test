import time


class CreateAccountPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element_by_id("firstName")
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.driver.find_element_by_id("lastName")
        last_name_field.send_keys(last_name)

    def enter_password(self, password):
        password_field = self.driver.find_element_by_name("Passwd")
        password_field.send_keys(password)

    def confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element_by_name("ConfirmPasswd")
        confirm_password_field.send_keys(confirm_password)

    def validate_username_field(self, email):
        validation_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."
        next_button = self.driver.find_element_by_id("accountDetailsNext")
        username_field = self.driver.find_element_by_id("username")
        username_field.clear()
        username_field.send_keys(email)
        next_button.click()
        time.sleep(1)
        assert validation_error in self.driver.page_source
