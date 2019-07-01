from selenium.webdriver.support.select import Select

from commands.TestSteps import TestSteps


class RegisterPage:
    register = {
        "personal_info": {
            "input_first_name": "css=#customer_firstname",
            "input_last_name": "css=#customer_lastname",
            "input_password": "css=#passwd"
        },
        "address": {
            "input_address": "css=#address1",
            "input_city": "css=#city",
            "select_state": "css=#id_state",
            "input_zip_code": "css=#postcode",
            "input_mobile_phone": "css=#phone_mobile"
        },
        "button_register": "css=#submitAccount"
    }

    def __init__(self):
        self.steps = TestSteps()

    def input_first_name(self, driver, first_name):
        self.steps.get_element(driver, self.register["personal_info"]["input_first_name"]).send_keys(first_name)

    def input_last_name(self, driver, last_name):
        self.steps.get_element(driver, self.register["personal_info"]["input_last_name"]).send_keys(last_name)

    def input_password(self, driver, password):
        self.steps.get_element(driver, self.register["personal_info"]["input_password"]).send_keys(password)

    def input_address(self, driver, address):
        self.steps.get_element(driver, self.register["address"]["input_address"]).send_keys(address)

    def input_city(self, driver, city):
        self.steps.get_element(driver, self.register["address"]["input_city"]).send_keys(city)

    def select_state(self, driver, state):
        locator = self.register["address"]["select_state"]
        Select(driver.find_element_by_css_selector(locator.split("css=")[1])).select_by_visible_text(state)

    def input_zip_code(self, driver, zip_code):
        self.steps.get_element(driver, self.register["address"]["input_zip_code"]).send_keys(zip_code)

    def input_mobile_phone(self, driver, mobile_phone):
        self.steps.get_element(driver, self.register["address"]["input_mobile_phone"]).send_keys(mobile_phone)

    def click_register_button(self, driver):
        self.steps.get_element(driver, self.register["button_register"]).click()
