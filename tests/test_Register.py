from commands.Utils import Utils
from commands.TestSteps import TestSteps
from commands.Assertions import Assertions
from page_objects import LoginPage
from page_objects import RegisterPage
from page_objects import HomePage


class TestRegister(object):
    utils = None
    config_data = None
    driver = None
    steps = None
    asserts = None
    login_page = None
    register_page = None
    home_page = None
    register_data = None

    @classmethod
    def setup_class(cls):
        cls.utils = Utils()
        cls.steps = TestSteps()
        cls.asserts = Assertions()
        cls.config_data = cls.utils.get_config_data()
        cls.driver = cls.utils.set_webdriver("chromedriver")
        cls.login_page = LoginPage.LoginPage()
        cls.register_page = RegisterPage.RegisterPage()
        cls.home_page = HomePage.HomePage()
        cls.register_data = cls.utils.get_test_data("register")

    @classmethod
    def teardown_class(cls):
        cls.utils.close_webdriver(cls.driver)

    def test_valid_registration(self):
        self.steps.navigate_to_url(self.driver, self.config_data["login_url"])
        register_email = self.utils.generate_test_email()
        register_first_name = self.utils.generate_test_first_name()
        register_last_name = self.utils.generate_test_last_name()
        register_address = self.utils.generate_test_street_address()
        register_city = self.utils.generate_test_city()
        register_state = self.utils.generate_test_state()
        register_zip_code = self.utils.generate_test_zip_code()
        register_mobile_phone = self.utils.generate_test_mobile_phone()
        self.login_page.input_register_email(self.driver, register_email)
        self.login_page.click_create_account_button(self.driver)
        self.register_page.input_first_name(self.driver, register_first_name)
        self.register_page.input_last_name(self.driver, register_last_name)
        self.register_page.input_password(self.driver, self.register_data["input_data"]["password"])
        self.register_page.input_address(self.driver, register_address)
        self.register_page.input_city(self.driver, register_city)
        self.register_page.select_state(self.driver, register_state)
        self.register_page.input_zip_code(self.driver, register_zip_code)
        self.register_page.input_mobile_phone(self.driver, register_mobile_phone)
        self.register_page.click_register_button(self.driver)
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.home_page.home["user_menu"]["label_my_account"]),
            register_first_name + " " + register_last_name)
