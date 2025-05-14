from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.main_page import MainPage
import time


def start_browser():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_login(driver):
    try:
        driver.get("https://okstra.socar.me/login?return_url=%2Fguest")
        time.sleep(1)

        login_page = LoginPage(driver)
        login_page.login("id", "pw")
        
        time.sleep(3)  # 로딩 시간 확보 (WebDriverWait 추천)

    finally:
        pass

def test_main():
    driver = start_browser()
    try:
        test_login(driver)
        main_page = MainPage(driver)
        main_page.open_reservation_creation_menu()
        
        time.sleep(3)  # 로딩 시간 확보 (WebDriverWait 추천)

    finally:
        pass


if __name__ == "__main__":
    test_main()