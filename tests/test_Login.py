import pytest

from commands.Utils import Utils
from commands.TestSteps import TestSteps
from commands.Assertions import Assertions
from page_objects import LoginPage
from page_objects import HomePage


class TestLogin(object):
    utils = None
    steps = None
    asserts = None
    login_page = None
    account_page = None
    config_data = None
    login_data = None
    driver = None

    @classmethod
    def setup_class(cls):
        cls.utils = Utils()
        cls.steps = TestSteps()
        cls.asserts = Assertions()
        cls.login_page = LoginPage.LoginPage()
        cls.home_page = HomePage.HomePage()
        cls.config_data = cls.utils.get_config_data()
        cls.login_data = cls.utils.get_test_data("login")
        cls.driver = cls.utils.set_webdriver("chromedriver")

    def setup_method(self):
        self.steps.navigate_to_url(self.driver, self.config_data["login_url"])

    @classmethod
    def teardown_class(cls):
        cls.utils.close_webdriver(cls.driver)

    @pytest.mark.smoke
    def test_valid_login(self):
        self.login_page.perform_login(self.driver, self.login_data["input_data"]["email"],
                                      self.login_data["input_data"]["password"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.home_page.home["user_menu"]["label_my_account"]),
            self.login_data["expected_data"]["account_name"])

    @pytest.mark.negative
    def test_blank_email_login(self):
        self.login_page.perform_login(self.driver, "", self.login_data["input_data"]["password"])
        self.asserts.verify_url(self.driver, self.config_data["login_url"].split('&')[0])
        self.asserts.verify_element_text(self.steps.get_element(self.driver, self.login_page.alert["label_spiel"]),
                                         self.login_data["expected_data"]["blank_email_login_error"])

    @pytest.mark.negative
    def test_blank_password_login(self):
        self.login_page.perform_login(self.driver, self.login_data["input_data"]["email"], "")
        self.asserts.verify_url(self.driver, self.config_data["login_url"].split('&')[0])
        self.asserts.verify_element_text(self.steps.get_element(self.driver, self.login_page.alert["label_spiel"]),
                                         self.login_data["expected_data"]["blank_password_login_error"])

    @pytest.mark.negative
    def test_invalid_email_login(self):
        self.login_page.perform_login(self.driver, self.login_data["input_data"]["invalid_email"],
                                      self.login_data["input_data"]["password"])
        self.asserts.verify_url(self.driver, self.config_data["login_url"].split('&')[0])
        self.asserts.verify_element_text(self.steps.get_element(self.driver, self.login_page.alert["label_spiel"]),
                                         self.login_data["expected_data"]["invalid_email_login_error"])

    @pytest.mark.negative
    def test_invalid_password_login(self):
        self.login_page.perform_login(self.driver, self.login_data["input_data"]["email"],
                                      self.login_data["input_data"]["invalid_password"])
        self.asserts.verify_url(self.driver, self.config_data["login_url"].split('&')[0])
        self.asserts.verify_element_text(self.steps.get_element(self.driver, self.login_page.alert["label_spiel"]),
                                         self.login_data["expected_data"]["invalid_password_login_error"])

    @pytest.mark.negative
    def test_short_password_login(self):
        self.login_page.perform_login(self.driver, self.login_data["input_data"]["email"],
                                      self.login_data["input_data"]["short_password"])
        self.asserts.verify_url(self.driver, self.config_data["login_url"].split('&')[0])
        self.asserts.verify_element_text(self.steps.get_element(self.driver, self.login_page.alert["label_spiel"]),
                                         self.login_data["expected_data"]["short_password_login_error"])
