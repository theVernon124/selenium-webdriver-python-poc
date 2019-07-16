import json
import os

from selenium import webdriver
from faker import Faker

_pwd = os.path.dirname(__file__).split("selenium-webdriver-python-poc")[0]


class Utils:

    def __init__(self):
        with open(_pwd + "selenium-webdriver-python-poc\\data\\config\\config.json") as json_file:
            self.config_data = json.load(json_file)
        self.fake = Faker()

    def get_config_data(self):
        return self.config_data

    def get_test_data(self, test_data_name):
        with open(_pwd + "selenium-webdriver-python-poc\\data\\test_data\\" + test_data_name + ".json") as json_file:
            return json.load(json_file)

    def set_webdriver(self, driver):
        driver = driver.lower()
        if driver == "chromedriver":
            driver_instance = webdriver.Chrome(self.config_data["chromedriver_path"])
            driver_instance.implicitly_wait(self.config_data["implicit_wait_timeout"])
            return driver_instance

    def close_webdriver(self, driver):
        driver.close()

    def generate_test_email(self):
        return self.fake.email()

    def generate_test_first_name(self):
        return self.fake.first_name()

    def generate_test_last_name(self):
        return self.fake.last_name()

    def generate_test_street_address(self):
        return self.fake.street_address()

    def generate_test_city(self):
        return self.fake.city()

    def generate_test_state(self):
        return self.fake.state()

    def generate_test_zip_code(self):
        return self.fake.postcode()

    def generate_test_mobile_phone(self):
        return self.fake.phone_number().split('x')[0]
