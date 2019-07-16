from commands.TestSteps import TestSteps


class LoginPage:

    login = {
        "input_email": "css=#email",
        "input_password": "css=#passwd",
        "button_sign_in": "css=#SubmitLogin"
    }
    register = {
        "input_email": "css=#email_create",
        "button_create_account": "css=#SubmitCreate",
        "label_error": "css=#create_account_error li"
    }
    alert = {
        "label_spiel": "css=div.alert-danger li"
    }

    def __init__(self):
        self.steps = TestSteps()

    def perform_login(self, driver, email, password):
        self.input_email_address(driver, email)
        self.input_password(driver, password)
        self.click_login_button(driver)

    def perform_create_account(self, driver, email):
        self.input_register_email(driver, email)
        self.click_create_account_button(driver)

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
