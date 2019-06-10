from commands.Utils import Utils
from commands.TestSteps import TestSteps
from commands.Assertions import Assertions
from page_objects import LoginPage
from page_objects import AccountPage

utils = Utils()
steps = TestSteps()
asserts = Assertions()
login_page = LoginPage.LoginPage()
account_page = AccountPage.AccountPage()
config_data = utils.get_config_data()
login_data = utils.get_test_data("login")
driver = utils.set_webdriver("chromedriver")
steps.navigate_to_url(driver, config_data["login_url"])
login_page.input_email_address(driver, login_data["input_data"]["email"])
login_page.input_password(driver, login_data["input_data"]["password"])
login_page.click_login_button(driver)
asserts.verify_element_text(driver.find_element_by_css_selector(account_page.account["header"]["label"]["locator"]),
                            login_data["expected_data"]["account_header"])
asserts.verify_element_text(driver.find_element_by_css_selector(account_page.account["user_menu"]["label"]["locator"]),
                            login_data["expected_data"]["account_name"])
utils.close_webdriver()
