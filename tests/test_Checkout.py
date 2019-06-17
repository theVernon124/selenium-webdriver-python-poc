from commands.TestSteps import TestSteps
from commands.Utils import Utils
from commands.Assertions import Assertions
from page_objects import HomePage
from page_objects import CartPage
from page_objects import LoginPage


class TestCheckout(object):
    steps = None
    utils = None
    asserts = None
    driver = None
    config_data = None
    checkout_data = None
    home_page = None
    cart_page = None
    login_page = None

    @classmethod
    def setup_class(cls):
        cls.steps = TestSteps()
        cls.utils = Utils()
        cls.asserts = Assertions()
        cls.driver = cls.utils.set_webdriver("chromedriver")
        cls.config_data = cls.utils.get_config_data()
        cls.checkout_data = cls.utils.get_test_data("checkout")
        cls.home_page = HomePage.HomePage()
        cls.cart_page = CartPage.CartPage()
        cls.login_page = LoginPage.LoginPage()

    @classmethod
    def teardown_class(cls):
        cls.utils.close_webdriver(cls.driver)

    def test_valid_checkout(self):
        self.steps.navigate_to_url(self.driver, self.config_data["home_url"])
        self.home_page.hover_on_product_card(self.driver, self.checkout_data["input_data"]["product_name"])
        self.home_page.click_add_to_cart_button(self.driver, self.checkout_data["input_data"]["product_name"])
        self.asserts.verify_element_visibility(self.driver, self.home_page.home["add_to_cart_modal"]["locator"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver,
                                   self.home_page.home["add_to_cart_modal"]["success"]["label"]["locator"]),
            self.checkout_data["expected_data"]["add_to_cart_success_spiel"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver,
                                   self.home_page.home["add_to_cart_modal"]["product"]["label"]["locator"]),
            self.checkout_data["expected_data"]["product_name"])
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver,
                                   self.home_page.home["add_to_cart_modal"]["cart_count"]["label"]["locator"]),
            self.checkout_data["expected_data"]["cart_count_spiel"])
        self.home_page.click_proceed_to_checkout_button(self.driver)
        self.asserts.verify_element_visibility(self.driver, self.cart_page.cart["header"]["label"]["locator"])
        self.asserts.verify_text_in_elements(
            self.driver, self.cart_page.cart["product"]["description"]["name"]["label"]["locator"],
            self.checkout_data["expected_data"]["cart_product_names"])
        self.asserts.verify_element_value(
            self.steps.get_generic_element(
                self.driver,
                self.cart_page.cart["product"]["quantity"]["input"]["locator"],
                self.checkout_data["input_data"]["product_name"]),
            self.checkout_data["expected_data"]["product_quantity"])
        self.cart_page.click_proceed_to_checkout_button(self.driver)
        self.login_page.input_email_address(self.driver, self.checkout_data["input_data"]["email"])
        self.login_page.input_password(self.driver, self.checkout_data["input_data"]["password"])
        self.login_page.click_login_button(self.driver)
        self.asserts.verify_element_text(
            self.steps.get_element(
                self.driver,
                self.cart_page.cart["address"]["delivery"]["name"]["label"]["locator"]),
            self.checkout_data["expected_data"]["customer_name"])
        self.asserts.verify_element_text(
            self.steps.get_element(
                self.driver,
                self.cart_page.cart["address"]["delivery"]["country"]["label"]["locator"]),
            self.checkout_data["expected_data"]["customer_country"])
        self.cart_page.click_checkout_button_from_address(self.driver)
        self.cart_page.tick_shipping_terms_of_service_checkbox(self.driver)
        self.cart_page.click_checkout_button_from_shipping(self.driver)
        self.asserts.verify_element_text(
            self.steps.get_generic_element(
                self.driver,
                self.cart_page.cart["payment"]["unit_price"]["label"]["locator"],
                self.checkout_data["input_data"]["product_name"]),
            self.checkout_data["expected_data"]["product_price"])
        self.asserts.verify_element_text(
            self.steps.get_generic_element(
                self.driver,
                self.cart_page.cart["payment"]["total"]["label"]["locator"],
                self.checkout_data["input_data"]["product_name"]),
            self.checkout_data["expected_data"]["product_total"])
        total_products = self.steps.get_element(
            self.driver, self.cart_page.cart["payment"]["total_products"]["label"]["locator"]).text
        total_shipping = self.steps.get_element(
            self.driver, self.cart_page.cart["payment"]["total_shipping"]["label"]["locator"]).text
        tax = self.steps.get_element(self.driver, self.cart_page.cart["payment"]["total_tax"]["label"]["locator"]).text
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.cart_page.cart["payment"]["cart_total"]["label"]["locator"]),
            '$' + str(
                float(total_products.split('$')[1]) + float(total_shipping.split('$')[1]) + float(tax.split('$')[1])))
        self.cart_page.click_pay_by_bankwire_button(self.driver)
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.cart_page.cart["payment"]["payment_channel"]["header"]["locator"]),
            self.checkout_data["expected_data"]["bankwire_header"])
        self.cart_page.click_confirm_order_button(self.driver)
        self.asserts.verify_element_text(
            self.steps.get_element(self.driver, self.cart_page.cart["payment"]["order_complete"]["label"]["locator"]),
            self.checkout_data["expected_data"]["order_complete_spiel"])
