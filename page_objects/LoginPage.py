from commands.TestSteps import TestSteps


class LoginPage:

    login = {
        "email": {
            "input": {
                "locator": "css=#email"
            }
        },
        "password": {
            "input": {
                "locator": "css=#passwd"
            }
        },
        "button": {
            "locator": "css=#SubmitLogin"
        }
    }

    def __init__(self):
        self.steps = TestSteps()

    def input_email_address(self, driver, email):
        self.steps.get_element(driver, self.login["email"]["input"]["locator"]).send_keys(email)

    def input_password(self, driver, password):
        self.steps.get_element(driver, self.login["password"]["input"]["locator"]).send_keys(password)

    def click_login_button(self, driver):
        self.steps.get_element(driver, self.login["button"]["locator"]).click()
