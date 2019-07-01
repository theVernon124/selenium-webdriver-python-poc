from commands.TestSteps import TestSteps


class HomePage:

    home = {
        "user_menu": {
            "label_my_account": "css=a[href='http://automationpractice.com/index.php?controller=my-account'] span"
        },
        "product_list": {
            "product_card": {
                "label": "xpath=//a[@class='product-name'][contains(text(), '{}')]",
                "button_add_to_cart": "xpath=//a[contains(text(), '{}')]/parent::h5/following-sibling::div[@class='button-container']/a[@title='Add to cart']"
            }
        },
        "add_to_cart_modal": {
            "locator": "css=#layer_cart",
            "label_success": "css=div.layer_cart_product h2",
            "label_product": "css=#layer_cart_product_title",
            "label_cart_count": "css=div.layer_cart_cart span.ajax_cart_product_txt",
            "button_checkout": "css=a[title='Proceed to checkout']"
        }
    }

    def __init__(self):
        self.steps = TestSteps()

    def hover_on_product_card(self, driver, product_name):
        product_card_locator = self.home["product_list"]["product_card"]["label"]
        self.steps.hover_on_element(driver, self.steps.get_element(driver, product_card_locator.format(product_name)))

    def click_add_to_cart_button(self, driver, product_name):
        add_to_cart_button_locator = self.home["product_list"]["product_card"]["button_add_to_cart"]
        self.steps.get_element(driver, add_to_cart_button_locator.format(product_name)).click()

    def click_proceed_to_checkout_button(self, driver):
        self.steps.get_element(driver, self.home["add_to_cart_modal"]["button_checkout"]).click()
