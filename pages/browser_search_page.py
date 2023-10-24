from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_project.pages.base_page import BasePage


class BrowserSearchPageLocators:
    SEARCH_INPUT = (By.ID, "APjFqb")
    FOUND_RESULT = (By.ID, "result-stats")
    LINK_POCHTA_RF = (By.CSS_SELECTOR, "a[href*='https://www.pochta.ru']")


class BrowserSearchPage(BasePage, BrowserSearchPageLocators):
    def click_in_search_input(self):
        self.find_element(*self.SEARCH_INPUT).click()

    def word_search_pochta_rf(self):
        self.find_element(*self.SEARCH_INPUT).send_keys("Почта РФ")

    def click_enter(self):
        self.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)

    def print_number_of_results_found(self):
        result = self.find_element(*self.FOUND_RESULT).text
        print(result)

    def click_in_result_search(self):
        link = self.find_element(*self.LINK_POCHTA_RF)
        original_window = self.driver.current_window_handle
        self.driver.execute_script("arguments[0].target='_blank';", link)
        link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.switch_to.window(original_window)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
