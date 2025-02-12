import allure
from data import Urls
from pages.password_recovery_page import PasswordRecoveryPage


@allure.story('Страница восстановления пароля')

class TestsPasswordRecovery:

    @allure.title('Проверка кнопки "показать/скрыть пароль" на странице восстановления пароля')
    @allure.description('Проверяем, что кнопка-глазок "показать/скрыть пароль" на странице восстановления пароля изменяет тип поля ввода пароля, делая символы видимым и невидимым.')
    def test_visibility_password_button(self, driver, user):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        recovery_page.enter_data_to_email_field(user['email'])
        recovery_page.click_to_recovery_button()
        recovery_page.click_to_password_visibility_button()
        assert recovery_page.check_password_active_frame()

    @allure.title('Переход на страницу восстановления пароля со страницы логина по кнопке «Восстановить пароль»')
    @allure.description('Проверяем, что со страницы логина можно перейти на страницу восстановления пароля, нажав на кнопку "Восстановить пароль", и на странице восстановления отображается кнопка "Восстановить".')
    def test_opening_to_password_recovery_page(self, driver):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_page(Urls.LOGIN_PAGE)
        recovery_page.click_to_password_recovery_button()
        assert (recovery_page.get_current_url() == Urls.FORGOT_PASSWORD_PAGE and
                recovery_page.get_header_from_recovery_button()) == 'Восстановить'

    @allure.title('Успешный запрос на восстановление пароля')
    @allure.description('Проверяем, что при вводе email и нажатии кнопки "Восстановить" происходит переход на страницу сброса пароля, и отображается заголовок "Восстановление пароля".')
    def test_entered_email_and_click_recovery(self, driver, user):
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open_page(Urls.FORGOT_PASSWORD_PAGE)
        recovery_page.enter_data_to_email_field(user['email'])
        recovery_page.click_to_recovery_button()
        recovery_page.wait_url_change(Urls.RESET_PASSWORD_PAGE)
        assert (recovery_page.get_current_url() == Urls.RESET_PASSWORD_PAGE and
                recovery_page.get_header_from_password_recovery() == 'Восстановление пароля')
