from commands.TestSteps import TestSteps


class HomePage:

    home = {
        "user_menu": {
            "my_account": {
                "label": {
                    "locator": "css=a[href='http://automationpractice.com/index.php?controller=my-account'] span"
                }
            }
        },
        "product_list": {
            "product_card": {
                "label": {
                    "locator": "xpath=//a[@class='product-name'][contains(text(), '{}')]"
                },
                "add_to_cart": {
                    "button": {
                        "locator": "xpath=//a[contains(text(), '{}')]/parent::h5/following-sibling::div[@class='button-container']/a[@title='Add to cart']"
                    }
                }
            }
        },
        "add_to_cart_modal": {
            "locator": "css=#layer_cart",
            "success": {
                "label": {
                    "locator": "css=div.layer_cart_product h2"
                }
            },
            "product": {
                "label": {
                    "locator": "css=#layer_cart_product_title"
                }
            },
            "cart_count": {
                "label": {
                    "locator": "css=div.layer_cart_cart span.ajax_cart_product_txt"
                }
            },
            "checkout": {
                "button": {
                    "locator": "css=a[title='Proceed to checkout']"
                }
            }
        }
    }

    def __init__(self):
        self.steps = TestSteps()

    def hover_on_product_card(self, driver, product_name):
        product_card_locator = self.home["product_list"]["product_card"]["label"]["locator"]
        self.steps.hover_on_element(driver, self.steps.get_element(driver, product_card_locator.format(product_name)))

    def click_add_to_cart_button(self, driver, product_name):
        add_to_cart_button_locator = self.home["product_list"]["product_card"]["add_to_cart"]["button"]["locator"]
        self.steps.get_element(driver, add_to_cart_button_locator.format(product_name)).click()

    def click_proceed_to_checkout_button(self, driver):
        self.steps.get_element(driver, self.home["add_to_cart_modal"]["checkout"]["button"]["locator"]).click()
