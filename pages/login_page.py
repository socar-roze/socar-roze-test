from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Chrome 드라이버 설정 (자동으로 설치)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username = (By.ID, "adminid")
        self.password = (By.ID, "password")
        self.login_button = (By.XPATH, '//*[@id="login_form"]/fieldset/input[2]')

    def login(self, username, password):
        # 아이디 입력
        self.driver.find_element(*self.username).send_keys(username)
        # 비밀번호 입력
        self.driver.find_element(*self.password).send_keys(password)
        # 로그인 버튼 클릭
        self.driver.find_element(*self.login_button).click()
        # 얼럿이 나타날 때까지 기다리고, 얼럿을 확인 (OK 버튼 클릭)
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()  # 확인 버튼 클릭
        print("확인눌렀다잉")

