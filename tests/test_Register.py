import pytest

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

    def setup_method(self):
        self.steps.navigate_to_url(self.driver, self.config_data["login_url"])

    @classmethod
    def teardown_class(cls):
        cls.utils.close_webdriver(cls.driver)

    @pytest.mark.smoke
    def test_valid_registration(self):
        register_email = self.utils.generate_test_email()
        register_first_name = self.utils.generate_test_first_name()
        register_last_name = self.utils.generate_test_last_name()
        register_address = self.utils.generate_test_street_address()
        register_city = self.utils.generate_test_city()
        register_state = self.utils.generate_test_state()
        register_zip_code = self.utils.generate_test_zip_code()
        register_mobile_phone = self.utils.generate_test_mobile_phone()
        self.login_page.perform_create_account(self.driver, register_email)
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

    @pytest.mark.negative
    def test_blank_email_create_account(self):
        self.login_page.perform_create_account(self.driver, "")
        self.asserts.verify_url(self.driver, self.config_data["login_url"])
        self.asserts.verify_element_text(self.steps.get_element(self.driver, self.login_page.register["label_error"]),
                                         self.register_data["expected_data"]["blank_email_create_account_error"])

    @pytest.mark.negative
    def test_invalid_email_create_account(self):
        self.login_page.perform_create_account(self.driver, self.register_data["input_data"]["invalid_email"])
        self.asserts.verify_url(self.driver, self.config_data["login_url"])
        self.asserts.verify_element_text(self.steps.get_element(self.driver, self.login_page.register["label_error"]),
                                         self.register_data["expected_data"]["invalid_email_create_account_error"])

    @pytest.mark.negative
    def test_short_email_create_account(self):
        self.login_page.perform_create_account(self.driver, self.register_data["input_data"]["short_email"])
        self.asserts.verify_url(self.driver, self.config_data["login_url"])
        self.asserts.verify_element_text(self.steps.get_element(self.driver, self.login_page.register["label_error"]),
                                         self.register_data["expected_data"]["short_email_create_account_error"])

    @pytest.mark.negative
    def test_existing_email_create_account(self):
        self.login_page.perform_create_account(self.driver, self.register_data["input_data"]["existing_email"])
        self.asserts.verify_url(self.driver, self.config_data["login_url"])
        self.asserts.verify_element_text(self.steps.get_element(self.driver, self.login_page.register["label_error"]),
                                         self.register_data["expected_data"]["existing_email_create_account_error"])

    @pytest.mark.negative
    def test_blank_personal_first_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(
            self.driver,
            self.register_page.generate_user_register_data(
                first_name="", password=self.register_data["input_data"]["password"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_first_name_register_error"])

    @pytest.mark.negative
    def test_blank_personal_last_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(
            self.driver,
            self.register_page.generate_user_register_data(
                last_name="", password=self.register_data["input_data"]["password"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_last_name_register_error"])

    @pytest.mark.negative
    def test_blank_personal_email_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]), email="")
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_email_register_error"])

    @pytest.mark.negative
    def test_blank_personal_password_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(password=""))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_password_register_error"])

    @pytest.mark.negative
    def test_blank_address_first_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]), address_first_name="")
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_address_first_name_register_error"])

    @pytest.mark.negative
    def test_blank_address_last_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]), address_last_name="")
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_address_last_name_register_error"])

    @pytest.mark.negative
    def test_blank_address_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"], address=""))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_address_register_error"])

    @pytest.mark.negative
    def test_blank_city_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"], city=""))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_city_register_error"])

    @pytest.mark.negative
    def test_blank_state_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"], state='-'))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_state_register_error"])

    @pytest.mark.negative
    def test_blank_zip_code_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"], zip_code=""))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_zip_code_register_error"])

    @pytest.mark.negative
    def test_blank_country_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]), country='-')
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_country_register_error"])

    @pytest.mark.negative
    def test_blank_mobile_phone_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"], mobile_phone=""))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_mobile_phone_register_error"])

    @pytest.mark.negative
    def test_blank_alias_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]), alias="")
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["blank_alias_register_error"])

    @pytest.mark.negative
    def test_invalid_personal_first_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            first_name=self.register_data["input_data"]["invalid_first_name"],
            password=self.register_data["input_data"]["password"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["invalid_personal_first_name_error"])

    @pytest.mark.negative
    def test_invalid_personal_last_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            last_name=self.register_data["input_data"]["invalid_last_name"],
            password=self.register_data["input_data"]["password"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["invalid_personal_last_name_error"])

    @pytest.mark.negative
    def test_invalid_email_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]),
                                            email=self.register_data["input_data"]["invalid_email"])
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["invalid_email_error"])

    @pytest.mark.negative
    def test_existing_email_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]),
                                            email=self.register_data["input_data"]["existing_email"])
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["existing_email_registration_error"])

    @pytest.mark.negative
    def test_invalid_address_first_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]),
                                            address_first_name=self.register_data["input_data"]["invalid_first_name"])
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["invalid_address_first_name_error"])

    @pytest.mark.negative
    def test_invalid_address_last_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]),
                                            address_last_name=self.register_data["input_data"]["invalid_last_name"])
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["invalid_address_last_name_error"])

    @pytest.mark.negative
    def test_invalid_address_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            address=self.register_data["input_data"]["invalid_address"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["invalid_address_error"])

    @pytest.mark.negative
    def test_invalid_city_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            city=self.register_data["input_data"]["invalid_city"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["invalid_city_error"])

    @pytest.mark.negative
    def test_invalid_zip_code_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            zip_code=self.register_data["input_data"]["invalid_zip_code"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["invalid_zip_code_error"])

    @pytest.mark.negative
    def test_invalid_mobile_phone(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            mobile_phone=self.register_data["input_data"]["invalid_mobile_phone"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["invalid_mobile_phone_error"])

    @pytest.mark.negative
    def test_long_personal_first_name(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            first_name=self.register_data["input_data"]["long_first_name"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["personal_first_name_length_error"])

    @pytest.mark.negative
    def test_long_personal_last_name(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            last_name=self.register_data["input_data"]["long_last_name"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["personal_last_name_length_error"])

    @pytest.mark.negative
    def test_short_password_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["short_password"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["short_password_error"])

    @pytest.mark.negative
    def test_long_password_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["long_password"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["long_password_error"])

    @pytest.mark.negative
    def test_long_address_first_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]),
                                            address_first_name=self.register_data["input_data"]["long_first_name"])
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["address_first_name_length_error"])

    @pytest.mark.negative
    def test_long_address_last_name_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]),
                                            address_last_name=self.register_data["input_data"]["long_last_name"])
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["address_last_name_length_error"])

    @pytest.mark.negative
    def test_long_address_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            address=self.register_data['input_data']["long_address"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["address_length_error"])

    @pytest.mark.negative
    def test_long_city_registration(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"], city=self.register_data["input_data"]["long_city"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["city_length_error"])

    @pytest.mark.negative
    def test_short_zip_code(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            zip_code=self.register_data["input_data"]["short_zip_code"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["zip_code_length_error"])

    @pytest.mark.negative
    def test_long_zip_code(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            zip_code=self.register_data["input_data"]["long_zip_code"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["zip_code_length_error"])

    @pytest.mark.negative
    def test_long_mobile_phone(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"],
            mobile_phone=self.register_data["input_data"]["long_mobile_phone"]))
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["mobile_phone_length_error"])

    @pytest.mark.negative
    def test_long_alias(self):
        register_email = self.utils.generate_test_email()
        self.login_page.perform_create_account(self.driver, register_email)
        self.register_page.perform_register(self.driver, self.register_page.generate_user_register_data(
            password=self.register_data["input_data"]["password"]),
                                            alias=self.register_data["input_data"]["long_alias"])
        self.asserts.verify_url(self.driver, self.config_data["register_url"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.register_page.register["label_error"]),
            self.register_data["expected_data"]["alias_length_error"])
