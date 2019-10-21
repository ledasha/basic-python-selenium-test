from selenium import webdriver
from src.create_account_page import CreateAccountPage
from src.sign_in_page import SignInPage

driver = webdriver.Chrome('C:\\temp\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://accounts.google.com")

sign_in_page = SignInPage(driver)
sign_in_page.click_create_account()

user_dictionary = {'fn': 'Darya', 'ln': 'Leanovich', 'password': 'Abc123456!'}
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}

create_account_page = CreateAccountPage(driver)
create_account_page.enter_first_name(user_dictionary['fn'])
create_account_page.enter_last_name(user_dictionary['ln'])
create_account_page.enter_password(user_dictionary['password'])
create_account_page.confirm_password(user_dictionary['password'])

for email in email_list:
    create_account_page.validate_username_field(email)

driver.quit()
