from selenium.webdriver.common.by import By

from test_project.pages.base_page import BasePage


class LoginPageLocators:
    BUTTON_LOGIN = (By.XPATH, "//span[text()='Войти']")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "userpassword")
    ERROR_MESSAGE = (By.ID, "usernameError")


class LoginPage(BasePage, LoginPageLocators):
    def checking_button_is_not_active(self):
        button_login = self.find_element(*self.BUTTON_LOGIN)
        is_disabled = button_login.get_attribute("disabled")
        assert not is_disabled, "Кнопка активна"

    def click_input_username(self):
        self.find_element(*self.USERNAME_INPUT).click()

    def check_input_username_is_clear(self):
        email_or_phone_field = self.find_element(*self.USERNAME_INPUT)
        email_or_phone_value = email_or_phone_field.get_attribute("value")
        assert not email_or_phone_value, "Поле 'Электронная почта или телефон' не пустое"

    def check_input_password_is_clear(self):
        password_field = self.find_element(*self.PASSWORD_INPUT)
        password_value = password_field.get_attribute("value")
        assert not password_value, "Поле 'Пароль' не пустое"

    def check_error_in_2_space(self):
        self.find_element(*self.USERNAME_INPUT).send_keys("  ")
        error = self.find_element(*self.ERROR_MESSAGE)
        error_text = error.text
        print(error_text)

    def check_error_incorrect_number(self):
        self.find_element(*self.USERNAME_INPUT).send_keys("98989898989")
        error = self.find_element(*self.ERROR_MESSAGE)
        error_text = error.text
        print(error_text)
