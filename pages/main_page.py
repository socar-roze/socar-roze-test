import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.reservation_menu = (By.XPATH, '//*[@id="oks-menu"]/ul/li[2]/a/span')
        self.reservation_sub_menu = (By.XPATH, '//*[@id="oks-menu"]/ul/li[2]/div/ul/li[1]/a')
        self.create_reservation_button = (By.CLASS_NAME, "reservation_id_btn")

    def open_reservation_creation_menu(self):

        # 예약 메뉴 - 예약 서브 메뉴 - 왕복 예약 생성 버튼 클릭
        self.driver.find_element(*self.reservation_menu).click()
        self.driver.find_element(*self.reservation_sub_menu).click()
        self.driver.find_element(*self.create_reservation_button).click()

        print("왕복 예약 모달 들어왔다잉")

        # 현재 창의 핸들을 저장
        main_window_handle = self.driver.current_window_handle

        # 모든 창 핸들을 가져와서 새 창으로 이동
        time.sleep(2)  # 창이 열릴 때까지 잠시 대기
        window_handles = self.driver.window_handles  # 열린 모든 창 핸들

        for handle in window_handles:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)  # 새 창으로 전환
                break

        print("왕복 예약 모달 새창 전환 했다잉")            



'''

# 3. '예약' 메뉴 클릭
reservation_menu = driver.find_element(By.XPATH, '//*[@id="oks-menu"]/ul/li[2]/a/span')  # '예약' 메뉴의 ID를 변경하세요.
reservation_menu.click()
reservation_sub_menu = driver.find_element(By.XPATH, '//*[@id="oks-menu"]/ul/li[2]/div/ul/li[1]/a')  # '예약' 메뉴의 ID를 변경하세요.
reservation_sub_menu.click()
print("예약 진입 완료!")


# 4. '왕복 예약' 버튼 클릭
create_reservation_button = driver.find_element(By.CLASS_NAME, "reservation_id_btn")  # '예약 생성' 버튼의 ID를 변경하세요.
create_reservation_button.click()

# 5. 예약 생성 새 창으로 이동 (새 창 핸들 저장)
# 현재 창의 핸들을 저장
main_window_handle = driver.current_window_handle

# 6. 새 창으로 이동
# 모든 창 핸들을 가져와서 새 창으로 이동
time.sleep(2)  # 창이 열릴 때까지 잠시 대기
window_handles = driver.window_handles  # 열린 모든 창 핸들

for handle in window_handles:
    if handle != main_window_handle:
        driver.switch_to.window(handle)  # 새 창으로 전환
        break



'''