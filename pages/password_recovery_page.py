import allure
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from selenium.webdriver.common.by import By


class PasswordRecoveryPage(BasePage):
    @allure.step('Клик на кнопку "Восстановить пароль" на странице логина')
    def click_to_password_recovery_button(self):
        self.move_to_element_and_click(PasswordRecoveryPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Клик на кнопку "Восстановить" на странице восстановления пароля')
    def click_to_recovery_button(self):
        self.move_to_element_and_click(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    @allure.step('Клик на глазок "показать/скрыть пароль" на странице восстановления пароля')
    def click_to_password_visibility_button(self):
        overlay_locator = (By.CSS_SELECTOR, '.Modal_modal_overlay__x2ZCr')
        self.wait_for_element_disappear(overlay_locator, time=10)
        self.click_to_element(PasswordRecoveryPageLocators.SHOW_PASSWORD_VISIBILITY_BUTTON)

    @allure.step('Ввод email в поле "Email" на странице восстановления пароля')
    def enter_data_to_email_field(self, data):
        self.enter_data(PasswordRecoveryPageLocators.EMAIL_INPUT_FIELD, data)

    @allure.step('Проверка активности поля "Пароль"')
    def check_password_active_frame(self):
        return self.find_element(PasswordRecoveryPageLocators.PASSWORD_INPUT_FIELD_ACTIVE_FRAME)

    @allure.step('Получение текста кнопки "Восстановить" на странице восстановления пароля')
    def get_header_from_recovery_button(self):
        return self.get_text_from_element(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    @allure.step('Получение текста заголовка "Восстановление пароля" на странице восстановления пароля')
    def get_header_from_password_recovery(self):
        return self.get_text_from_element(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_PAGE_HEADER)
