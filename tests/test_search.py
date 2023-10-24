import allure

from test_project.pages.browser_search_page import BrowserSearchPage
from test_project.pages.login_page import LoginPage
from test_project.pages.mail_page import MailPage
from test_project.pages.pochta_search_page import SearchPage


@allure.story('Поиск и переход на страницу результатов')
def test_search_pochta_rf(browser_session):
    with allure.step('Открыть страницу поисковика'):
        search_page = BrowserSearchPage(browser_session)
        search_page.click_in_search_input()

    with allure.step('Ввести запрос "pochta.ru" и выполнить поиск'):
        search_page.word_search_pochta_rf()
        search_page.click_enter()

    with allure.step('Вывести количество найденных результатов'):
        search_page.print_number_of_results_found()

    with allure.step('Кликнуть по первому результату поиска и закрыть вкладку с поисковой системой'):
        search_page.click_in_result_search()


@allure.story("Проверка интерактивности и валидации формы входа")
def test_login_form_interaction_and_validation(browser_session):
    with allure.step("Перейти на страницу входа в почтовый ящик"):
        mail_page = MailPage(browser_session)
        mail_page.click_in_button_login()

    with allure.step("Проверка полей формы входа и кнопки входа"):
        login_page = LoginPage(browser_session)
        login_page.check_input_username_is_clear()
        login_page.check_input_password_is_clear()
        login_page.checking_button_is_not_active()


@allure.story("Проверка ошибки при двух пробелах в поле ввода")
def test_check_error_2_space(browser_session):
    with allure.step("Открыть страницу входа и ввести два пробела в поле ввода"):
        login_page = LoginPage(browser_session)
        login_page.click_input_username()
        login_page.check_error_in_2_space()


@allure.story("Проверка ошибки при вводе некорректного номера телефона")
def test_incorrect_number(browser_session):
    with allure.step("Открыть страницу входа и ввести некорректный номер телефона"):
        login_page = LoginPage(browser_session)
        login_page.click_input_username()
        login_page.check_error_incorrect_number()


@allure.story("Поиск информационного блока")
def test_search_info_block(browser):
    with allure.step("Вернуться на главную страницу почты и начать поиск"):
        mail_page = MailPage(browser)
        mail_page.return_in_mail_page()

    with allure.step("Выполнить поиск по сайту, в поле ввести «Совкомбанк»"):
        mail_page.click_in_search_button()
        mail_page.enter_text_search()
        mail_page.click_seacrh_button_in_input()

    with allure.step(
        "В результатах поиска проверить, что значение в поле совпадает со значением в информационном блоке"
    ):
        search_pochta_page = SearchPage(browser)
        search_pochta_page.check_field_matches_info_block()


@allure.story("Переход по разделам и сбор плейсхолдеров")
def test_navigation_and_collecting_placeholders(browser):
    with allure.step("Вернуться на главную страницу и перейти в меню"):
        mail_page = MailPage(browser)
        mail_page.return_in_mail_page()

    with allure.step("Навести курсор мыши на верхнее меню «Отправить»"):
        mail_page.move_in_menu()

    with allure.step("Выбрать вариант «Посылку»"):
        mail_page.click_choise_in_menu()

    with allure.step("Собрать информацию о плейсхолдерах"):
        mail_page.get_buttons_info()
