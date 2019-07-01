from commands.TestSteps import TestSteps


class LoginPage:

    login = {
        "input_email": "css=#email",
        "input_password": "css=#passwd",
        "button_sign_in": "css=#SubmitLogin"
    }
    register = {
        "input_email": "css=#email_create",
        "button_create_account": "css=#SubmitCreate"
    }

    def __init__(self):
        self.steps = TestSteps()

    def input_email_address(self, driver, email):
        self.steps.get_element(driver, self.login["input_email"]).send_keys(email)

    def input_password(self, driver, password):
        self.steps.get_element(driver, self.login["input_password"]).send_keys(password)

    def input_register_email(self, driver, email):
        self.steps.get_element(driver, self.register["input_email"]).send_keys(email)

    def click_login_button(self, driver):
        self.steps.get_element(driver, self.login["button_sign_in"]).click()

    def click_create_account_button(self, driver):
        self.steps.get_element(driver, self.register["button_create_account"]).click()
