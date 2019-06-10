from selenium import webdriver
import json, os
_pwd = os.path.dirname(__file__).split("selenium-webdriver-python-poc")[0]


class Utils:

    def __init__(self):
        with open(_pwd + "selenium-webdriver-python-poc\\data\\config\\config.json") as json_file:
            self.config_data = json.load(json_file)

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
