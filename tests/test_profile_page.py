import allure
from data import Urls
from pages.profile_page import ProfilePage

@allure.story('Личный кабинет пользователя')

class TestProfilePage:

    @allure.title('Переход в личный кабинет неавторизованным пользователем')
    @allure.description('Проверяем, что неавторизованный пользователь при попытке перехода в личный кабинет перенаправляется на страницу логина.')
    def test_go_to_profile_page(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.open_page(Urls.BASE_PAGE)
        profile_page.click_lk_button()
        profile_page.wait_url_change(Urls.LOGIN_PAGE)
        assert (profile_page.get_current_url() == Urls.LOGIN_PAGE and
                profile_page.get_text_password_recovery_button() == 'Восстановить пароль')

    @allure.title('Переход в раздел "История заказов" в личном кабинете')
    @allure.description('Проверяем, что авторизованный пользователь может перейти в раздел "История заказов" в личном кабинете, и URL страницы соответствует странице истории заказов.')
    def test_go_to_orders_history(self, driver, user):
        profile_page = ProfilePage(driver)
        profile_page.open_page(Urls.LOGIN_PAGE)
        profile_page.login(user)
        profile_page.wait_url_change(Urls.BASE_PAGE)
        profile_page.click_lk_button()
        profile_page.wait_url_change(Urls.ACCOUNT_PROFILE_PAGE)
        profile_page.click_order_history_button()
        assert profile_page.get_current_url() == Urls.ORDER_HISTORY_PAGE

    @allure.title('Выход из аккаунта пользователя в личном кабинете')
    @allure.description('Проверяем, что авторизованный пользователь может выйти из аккаунта через личный кабинет, и после выхода происходит перенаправление на страницу логина.')
    def test_logout(self, driver, user):
        profile_page = ProfilePage(driver)
        profile_page.open_page(Urls.LOGIN_PAGE)
        profile_page.login(user)
        profile_page.wait_url_change(Urls.BASE_PAGE)
        profile_page.click_lk_button()
        profile_page.wait_url_change(Urls.ACCOUNT_PROFILE_PAGE)
        profile_page.click_logout_button()
        assert (profile_page.get_text_login_button() == 'Войти'
                and profile_page.get_current_url() == Urls.LOGIN_PAGE)
