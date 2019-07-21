from commands.TestSteps import TestSteps


class CartPage:
    cart = {
        "header": "css=#cart_title",
        "product": {
            "description": {
                "label_name": "css=tr.cart_item td.cart_description p.product-name a"
            },
            "input_quantity": "xpath=//a[text()='{}']/ancestor::td[@class='cart_description']/following-sibling::td[contains(@class, 'cart_quantity')]/input[contains(@class, 'cart_quantity_input')]"
        },
        "button_proceed_to_checkout": "css=a.standard-checkout",
        "address": {
            "delivery": {
                "label_name": "css=#address_delivery li.address_firstname",
                "label_country": "css=#address_delivery li.address_country_name"
            },
            "button_proceed_to_checkout": "css=button[name='processAddress']"
        },
        "shipping": {
            "checkbox_terms_of_service": "css=#cgv",
            "button_proceed_to_checkout": "css=button[name='processCarrier']",
            "label_shipping_error": "css=p.fancybox-error"
        },
        "payment": {
            "label_unit_price": "xpath=//a[text()='{}']/ancestor::td[@class='cart_description']/following-sibling::td[@class='cart_unit']/span[@class='price']",
            "label_total": "xpath=//a[text()='{}']/ancestor::td[@class='cart_description']/following-sibling::td[@class='cart_total']/span[@class='price']",
            "label_total_products": "css=#total_product",
            "label_total_shipping": "css=#total_shipping",
            "label_total_tax": "css=#total_tax",
            "label_cart_total": "css=#total_price_container",
            "button_pay_by_bankwire": "css=a.bankwire",
            "header_payment_channel": "css=h3.page-subheading",
            "button_confirm_order": "css=button.button-medium[type='submit']",
            "label_order_complete": "css=p.cheque-indent strong"
        }
    }

    def __init__(self):
        self.steps = TestSteps()

    def click_proceed_to_checkout_button(self, driver):
        self.steps.get_element(driver, self.cart["button_proceed_to_checkout"]).click()

    def click_checkout_button_from_address(self, driver):
        self.steps.get_element(driver, self.cart["address"]["button_proceed_to_checkout"]).click()

    def click_checkout_button_from_shipping(self, driver):
        self.steps.get_element(driver, self.cart["shipping"]["button_proceed_to_checkout"]).click()

    def click_pay_by_bankwire_button(self, driver):
        self.steps.get_element(driver, self.cart["payment"]["button_pay_by_bankwire"]).click()

    def click_confirm_order_button(self, driver):
        self.steps.get_element(driver, self.cart["payment"]["button_confirm_order"]).click()

    def tick_shipping_terms_of_service_checkbox(self, driver):
        tos_checkbox_locator = self.cart["shipping"]["checkbox_terms_of_service"]
        driver.find_element_by_css_selector(tos_checkbox_locator.split("css=")[1]).click()
