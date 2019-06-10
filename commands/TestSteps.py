class TestSteps:

    def navigate_to_url(self, driver, url):
        driver.get(url)

    def scroll_element_into_view(self, driver, element):
        driver.execute_script("arguments[0].scrollIntoView();", element)
