import pytest
from selenium import webdriver

from test_project.config import MAIN_URL


@pytest.fixture(scope="session")
def browser_session(request):
    driver = webdriver.Chrome()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture
def browser(request):
    driver = webdriver.Chrome()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()
