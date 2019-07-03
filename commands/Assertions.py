from commands.TestSteps import TestSteps


class Assertions:
    steps = TestSteps()

    def verify_element_text(self, element, expected_text):
        assert expected_text in element.text, element.text + " did not equal '" + expected_text + "'."

    def verify_element_visibility(self, driver, locator, should_be_visible=True):
        if should_be_visible:
            assert self.steps.get_element(driver, locator) is not None, \
                "Expected: Element " + locator + " is visible. Actual: Element was not visible."
        else:
            assert self.steps.get_element(driver, locator) is None, \
                "Expected: Element " + locator + " is not visible. Actual: Element was visible."

    def verify_text_in_elements(self, driver, locator, expected_texts):
        element_texts = []
        for element in self.steps.get_elements(driver, locator):
            element_texts.append(element.text)
        for text in expected_texts:
            assert text in element_texts, \
                "Expected: " + text + " in " + element_texts + ". Actual: Text was not in list."

    def verify_element_value(self, element, expected_value):
        assert expected_value in element.get_attribute("value"), \
            "Expected element value: " + expected_value + ". Actual: " + element.get_attribute("value")

    def verify_url(self, driver, expected_url):
        assert expected_url in driver.current_url
