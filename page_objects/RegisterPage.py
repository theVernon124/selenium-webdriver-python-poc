from selenium.webdriver.support.select import Select

from commands.TestSteps import TestSteps
from commands.Utils import Utils


class RegisterPage:
    register = {
        "label_error": "css=div.alert-danger li:nth-child(1)",
        "personal_info": {
            "input_first_name": "css=#customer_firstname",
            "input_last_name": "css=#customer_lastname",
            "input_email": "css=#email",
            "input_password": "css=#passwd"
        },
        "address": {
            "input_first_name": "css=#firstname",
            "input_last_name": "css=#lastname",
            "input_address": "css=#address1",
            "input_city": "css=#city",
            "input_zip_code": "css=#postcode",
            "input_mobile_phone": "css=#phone_mobile",
            "input_alias": "css=#alias",
            "select_state": "css=#id_state",
            "select_country": "css=#id_country"
        },
        "button_register": "css=#submitAccount"
    }

    def __init__(self):
        self.steps = TestSteps()
        self.utils = Utils()

    def generate_user_register_data(self, first_name=None, last_name=None, password=None, address=None, city=None,
                                    state=None, zip_code=None, mobile_phone=None):
        data = {}
        data["first_name"] = self.utils.generate_test_first_name() if first_name is None else first_name
        data["last_name"] = self.utils.generate_test_last_name() if last_name is None else last_name
        data["password"] = password
        data["address"] = self.utils.generate_test_street_address() if address is None else address
        data["city"] = self.utils.generate_test_city() if city is None else city
        data["state"] = self.utils.generate_test_state() if state is None else state
        data["zip_code"] = self.utils.generate_test_zip_code() if zip_code is None else zip_code
        data["mobile_phone"] = self.utils.generate_test_mobile_phone() if mobile_phone is None else mobile_phone
        return data

    def perform_register(self, driver, user_register_data, email=None, address_first_name=None, address_last_name=None,
                         country=None, alias=None):
        self.input_first_name(driver, user_register_data["first_name"])
        self.input_last_name(driver, user_register_data["last_name"])
        if email is not None:
            self.input_email(driver, email)
        self.input_password(driver, user_register_data["password"])
        if address_first_name is not None:
            self.input_address_first_name(driver, address_first_name)
        if address_last_name is not None:
            self.input_address_last_name(driver, address_last_name)
        self.input_address(driver, user_register_data["address"])
        self.input_city(driver, user_register_data["city"])
        self.select_state(driver, user_register_data["state"])
        self.input_zip_code(driver, user_register_data["zip_code"])
        if country is not None:
            self.select_country(driver, country)
        self.input_mobile_phone(driver, user_register_data["mobile_phone"])
        if alias is not None:
            self.input_alias(driver, alias)
        self.click_register_button(driver)

    def input_first_name(self, driver, first_name):
        self.steps.get_element(driver, self.register["personal_info"]["input_first_name"]).send_keys(first_name)

    def input_last_name(self, driver, last_name):
        self.steps.get_element(driver, self.register["personal_info"]["input_last_name"]).send_keys(last_name)

    def input_email(self, driver, email):
        element = self.steps.get_element(driver, self.register["personal_info"]["input_email"])
        element.clear()
        element.send_keys(email)

    def input_password(self, driver, password):
        self.steps.get_element(driver, self.register["personal_info"]["input_password"]).send_keys(password)

    def input_address_first_name(self, driver, first_name):
        element = self.steps.get_element(driver, self.register["address"]["input_first_name"])
        element.clear()
        element.send_keys(first_name)

    def input_address_last_name(self, driver, last_name):
        element = self.steps.get_element(driver, self.register["address"]["input_last_name"])
        element.clear()
        element.send_keys(last_name)

    def input_address(self, driver, address):
        self.steps.get_element(driver, self.register["address"]["input_address"]).send_keys(address)

    def input_city(self, driver, city):
        self.steps.get_element(driver, self.register["address"]["input_city"]).send_keys(city)

    def input_zip_code(self, driver, zip_code):
        self.steps.get_element(driver, self.register["address"]["input_zip_code"]).send_keys(zip_code)

    def input_mobile_phone(self, driver, mobile_phone):
        self.steps.get_element(driver, self.register["address"]["input_mobile_phone"]).send_keys(mobile_phone)

    def input_alias(self, driver, alias):
        element = self.steps.get_element(driver, self.register["address"]["input_alias"])
        element.clear()
        element.send_keys(alias)

    def select_state(self, driver, state):
        locator = self.register["address"]["select_state"]
        Select(driver.find_element_by_css_selector(locator.split("css=")[1])).select_by_visible_text(state)

    def select_country(self, driver, country):
        locator = self.register["address"]["select_country"]
        Select(driver.find_element_by_css_selector(locator.split("css=")[1])).select_by_visible_text(country)

    def click_register_button(self, driver):
        self.steps.get_element(driver, self.register["button_register"]).click()
