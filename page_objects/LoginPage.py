from commands.TestSteps import TestSteps


class LoginPage:

    login = {
        "email": {
            "input": {
                "locator": "input[name='username']"
            }
        },
        "password": {
            "input": {
                "locator": "input[name='password']"
            }
        },
        "button": {
            "locator": "button.loginbtn"
        }
    }

    def __init__(self):
        self.steps = TestSteps()

    def input_email_address(self, driver, email):
        driver.find_element_by_css_selector(self.login["email"]["input"]["locator"]).send_keys(email)

    def input_password(self, driver, password):
        driver.find_element_by_css_selector(self.login["password"]["input"]["locator"]).send_keys(password)

    def click_login_button(self, driver):
        element = driver.find_element_by_css_selector(self.login["button"]["locator"])
        self.steps.scroll_element_into_view(driver, element)
        element.click()
