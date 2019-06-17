from commands.TestSteps import TestSteps


class CartPage:
    cart = {
        "header": {
            "label": {
                "locator": "css=#cart_title"
            }
        },
        "product": {
            "description": {
                "name": {
                    "label": {
                        "locator": "css=tr.cart_item td.cart_description p.product-name a"
                    }
                }
            },
            "quantity": {
                "input": {
                    "locator": "xpath=//a[text()='{}']/ancestor::td[@class='cart_description']/following-sibling::td[contains(@class, 'cart_quantity')]/input[contains(@class, 'cart_quantity_input')]"
                }
            }
        },
        "proceed_to_checkout": {
            "button": {
                "locator": "css=a.standard-checkout"
            }
        },
        "address": {
            "delivery": {
                "name": {
                    "label": {
                        "locator": "css=#address_delivery li.address_firstname"
                    }
                },
                "country": {
                    "label": {
                        "locator": "css=#address_delivery li.address_country_name"
                    }
                }
            },
            "proceed_to_checkout": {
                "button": {
                    "locator": "css=button[name='processAddress']"
                }
            }
        },
        "shipping": {
            "terms_of_service": {
                "checkbox": {
                    "locator": "css=#cgv"
                }
            },
            "proceed_to_checkout": {
                "button": {
                    "locator": "css=button[name='processCarrier']"
                }
            }
        },
        "payment": {
            "unit_price": {
                "label": {
                    "locator": "xpath=//a[text()='{}']/ancestor::td[@class='cart_description']/following-sibling::td[@class='cart_unit']/span[@class='price']"
                }
            },
            "total": {
                "label": {
                    "locator": "xpath=//a[text()='{}']/ancestor::td[@class='cart_description']/following-sibling::td[@class='cart_total']/span[@class='price']"
                }
            },
            "total_products": {
                "label": {
                    "locator": "css=#total_product"
                }
            },
            "total_shipping": {
                "label": {
                    "locator": "css=#total_shipping"
                }
            },
            "total_tax": {
                "label": {
                    "locator": "css=#total_tax"
                }
            },
            "cart_total": {
                "label": {
                    "locator": "css=#total_price_container"
                }
            },
            "pay_by_bankwire": {
                "button": {
                    "locator": "css=a.bankwire"
                }
            },
            "payment_channel": {
                "header": {
                    "locator": "css=h3.page-subheading"
                }
            },
            "confirm_order": {
                "button": {
                    "locator": "css=button.button-medium[type='submit']"
                }
            },
            "order_complete": {
                "label": {
                    "locator": "css=p.cheque-indent strong"
                }
            }
        }
    }

    def __init__(self):
        self.steps = TestSteps()

    def click_proceed_to_checkout_button(self, driver):
        self.steps.get_element(driver, self.cart["proceed_to_checkout"]["button"]["locator"]).click()

    def click_checkout_button_from_address(self, driver):
        self.steps.get_element(driver, self.cart["address"]["proceed_to_checkout"]["button"]["locator"]).click()

    def click_checkout_button_from_shipping(self, driver):
        self.steps.get_element(driver, self.cart["shipping"]["proceed_to_checkout"]["button"]["locator"]).click()

    def click_pay_by_bankwire_button(self, driver):
        self.steps.get_element(driver, self.cart["payment"]["pay_by_bankwire"]["button"]["locator"]).click()

    def click_confirm_order_button(self, driver):
        self.steps.get_element(driver, self.cart["payment"]["confirm_order"]["button"]["locator"]).click()

    def tick_shipping_terms_of_service_checkbox(self, driver):
        tos_checkbox_locator = self.cart["shipping"]["terms_of_service"]["checkbox"]["locator"]
        driver.find_element_by_css_selector(tos_checkbox_locator.split("css=")[1]).click()
