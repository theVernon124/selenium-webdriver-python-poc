from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class TestSteps:

    def navigate_to_url(self, driver, url):
        driver.get(url)

    def scroll_element_into_view(self, driver, element):
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_element(self, driver, locator, timeout=15):
        try:
            if locator.startswith("css="):
                return wait(driver, timeout).until(
                    ec.visibility_of_element_located((By.CSS_SELECTOR, locator.split("css=")[1])))
            elif locator.startswith("xpath="):
                return wait(driver, timeout).until(
                    ec.visibility_of_element_located((By.XPATH, locator.split("xpath=")[1])))
        except NoSuchElementException:
            return None

    def get_elements(self, driver, locator):
        try:
            if locator.startswith("css="):
                return driver.find_elements_by_css_selector(locator.split("css=")[1])
            elif locator.startswith("xpath="):
                return driver.find_elements_by_css_selector(locator.split("xpath=")[1])
        except NoSuchElementException:
            return None

    def get_generic_element(self, driver, locator, element_identifier, timeout=15):
        try:
            if locator.startswith("css="):
                return wait(driver, timeout).until(ec.visibility_of_element_located(
                    (By.CSS_SELECTOR, locator.split("css=")[1].format(element_identifier))))
            elif locator.startswith("xpath="):
                return wait(driver, timeout).until(
                    ec.visibility_of_element_located((By.XPATH, locator.split("xpath=")[1].format(element_identifier))))
        except NoSuchElementException:
            return None

    def hover_on_element(self, driver, element):
        ActionChains(driver).move_to_element(element).perform()
