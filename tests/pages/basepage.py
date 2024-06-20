from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://sbis.ru/'
        self.actions = ActionChains(self.driver)

    def find_element(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def switch_window_close_origin(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return self.driver.current_window_handle
