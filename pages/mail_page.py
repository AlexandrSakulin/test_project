from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from test_project.pages.base_page import BasePage


class MailPageLocators:
    BUTTON_LOGIN = (By.XPATH, "//a[text()='Войти']")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "svg[role='button'][tabindex='0']")
    INPUT_SEARCH = (By.XPATH, "//div[@data-submenu='submenu'][@data-testid='submenu']//input[@type='text']")
    BUTTON_SEARCH_IN_INPUT = (By.CSS_SELECTOR, "svg[data-testid='search-button']")
    MENU_BUTTON_SEND = (By.XPATH, "//a[@data-submenu='submenu' and text()='Отправить']")
    SEND_BUTTON = (By.CSS_SELECTOR, "div[data-submenu='submenu'] a[href='/parcels']")
    BLOCK_BUTTONS = (By.CSS_SELECTOR, "div[data-testid='parcels.options-tabs']")


class MailPage(BasePage, MailPageLocators):
    def click_in_button_login(self):
        login_button = self.find_element(*self.BUTTON_LOGIN)
        self.driver.execute_script("arguments[0].click();", login_button)

    def return_in_mail_page(self):
        self.driver.get("https://www.pochta.ru/")

    def click_in_search_button(self):
        self.find_element(*self.BUTTON_SEARCH).click()

    def enter_text_search(self):
        self.find_element(*self.INPUT_SEARCH).send_keys("Совкомбанк")

    def click_seacrh_button_in_input(self):
        self.find_element(*self.BUTTON_SEARCH_IN_INPUT).click()

    def move_in_menu(self):
        menu = self.find_element(*self.MENU_BUTTON_SEND)
        actions = ActionChains(self.driver)
        actions.move_to_element(menu).perform()

    def click_choise_in_menu(self):
        self.find_element(*self.SEND_BUTTON).click()

    def get_buttons_info(self):
        parent_element = self.find_element(By.CSS_SELECTOR, 'div[data-testid="parcels.options-tabs"]')
        labels = parent_element.find_elements(By.CSS_SELECTOR, "label")
        result = {}
        for label in labels:
            label.click()
            input_or_textarea = label.find_element(
                By.XPATH, ".//following::input[@placeholder][1] | .//following::textarea[@placeholder][1]"
            )
            placeholder = input_or_textarea.get_attribute("placeholder")
            result[label.text] = placeholder
        print(result)
