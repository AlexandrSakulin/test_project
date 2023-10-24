from selenium.webdriver.common.by import By

from test_project.pages.base_page import BasePage


class SearchPageLocators:
    INPUT_SEARCH = (By.XPATH, "//input[@placeholder='Поиск по сайту']")
    OUTPUT_SEARCH = (By.XPATH, "//div[contains(@class, 'Notificationstyles')]//span")


class SearchPage(BasePage, SearchPageLocators):
    def check_field_matches_info_block(self):
        input_element = self.find_element(*self.INPUT_SEARCH)
        input_value = input_element.get_attribute("value")
        output_element = self.find_element(*self.OUTPUT_SEARCH)
        output_text = output_element.text
        assert input_value in output_text, "Значение в поле не совпадает со значением в информационном блоке"
