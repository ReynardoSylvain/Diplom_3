import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators


class ProfilePage(BasePage):
    @allure.step('Клик на кнопку "Личный кабинет" в хедере')
    def click_lk_button(self):
        self.move_to_element_and_click(MainPageLocators.BUTTON_ACCOUNT)

    @allure.step('Авторизация пользователя')
    def login(self, data):
        self.enter_data(ProfilePageLocators.EMAIL_INPUT_FIELD, data['email'])
        self.enter_data(ProfilePageLocators.PASSWORD_INPUT_FIELD, data['password'])
        self.move_to_element_and_click(ProfilePageLocators.LOGIN_BUTTON)

    @allure.step('Клик на кнопку "История заказов" в личном кабинете')
    def click_order_history_button(self):
        self.move_to_element_and_click(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Клик на кнопку "Выход" в личном кабинете')
    def click_logout_button(self):
        self.move_to_element_and_click(ProfilePageLocators.EXIT_BUTTON)

    @allure.step('Получение текста кнопки "Восстановить пароль" на странице логина')
    def get_text_password_recovery_button(self):
        return self.get_text_from_element(PasswordRecoveryPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Получение текста кнопки "Войти" на странице логина')
    def get_text_login_button(self):
        return self.get_text_from_element(ProfilePageLocators.LOGIN_BUTTON)
