from commands.TestSteps import TestSteps


class ProductPage:
    product = {
        "input_quantity": "css=#quantity_wanted",
        "label_product_error": "css=p.fancybox-error",
        "button_add_to_cart": "css=button[name='Submit']"
    }

    def __init__(self):
        self.steps = TestSteps()

    def input_quantity(self, driver, quantity):
        element = self.steps.get_element(driver, self.product["input_quantity"])
        element.clear()
        element.send_keys(quantity)

    def click_add_to_cart_button(self, driver):
        self.steps.get_element(driver, self.product["button_add_to_cart"]).click()
