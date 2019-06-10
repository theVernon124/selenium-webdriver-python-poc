class Assertions:

    def verify_element_text(self, element, expected_text):
        assert expected_text in element.text, element.text + " did not equal '" + expected_text + "'."
