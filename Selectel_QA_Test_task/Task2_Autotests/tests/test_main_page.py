import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_open_main_page(driver):
    driver.get("https://selectel.ru")
    assert "Selectel" in driver.title


def test_login_button_present(driver):
    driver.get("https://selectel.ru")

    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Войти"))
    )

    assert login_button.is_displayed()


def test_navigation_menu_present(driver):
    driver.get("https://selectel.ru")

    wait = WebDriverWait(driver, 10)
    header = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "header"))
    )

    assert header.is_displayed()


def test_scroll_to_bottom(driver):
    driver.get("https://selectel.ru")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    assert True


def test_page_title_not_empty(driver):
    driver.get("https://selectel.ru")

    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: d.title != "")

    assert driver.title != ""