import allure
import helper
from data import Urls
from pages.order_list_page import OrderList
from pages.profile_page import ProfilePage
from pages.main_page import MainPage


@allure.story('Страница ленты заказов')

class TestOrderList:

    @allure.title('Открытие всплывающего окна с деталями заказа из ленты заказов')
    @allure.description('Проверяем, что при клике на заказ в ленте заказов открывается всплывающее окно с деталями заказа.')
    def test_order_details_window(self, driver):
        order_page = OrderList(driver)
        order_page.open_page(Urls.BASE_PAGE)
        main_page = MainPage(driver)
        main_page.click_to_order_list_button()
        order_page.click_on_order()
        assert order_page.get_text_from_details() == 'Cостав'

    @allure.title('Отображение созданного заказа пользователя в ленте и истории заказов')
    @allure.description('Проверяем что заказ созданный пользователем, отображается в ленте заказов и в истории заказов.')
    def test_created_orders_in_order_history(self, driver, user):
        order_page = OrderList(driver)
        order_page.open_page(Urls.LOGIN_PAGE)
        response = helper.create_order(user)
        order_number = response.json()['order']['number']
        profile_page = ProfilePage(driver)
        profile_page.login(user)
        profile_page.wait_url_change(Urls.BASE_PAGE)
        main_page = MainPage(driver)
        main_page.click_to_order_list_button()
        order_page.search_element_by_order_number(order_number)
        profile_page.click_lk_button()
        profile_page.wait_url_change(Urls.ACCOUNT_PROFILE_PAGE)
        profile_page.click_order_history_button()
        assert str(order_number) in order_page.get_order_number()

    @allure.title('Проверка счетчика "Выполнено за все время" в ленте заказов')
    @allure.description('Проверяем, что счетчик "Выполнено за все время" увеличивается после создания нового заказа.')
    def test_all_time_counter(self, driver, user):
        order_page = OrderList(driver)
        order_page.open_page(Urls.ORDER_LIST_PAGE)
        old_counter = order_page.get_all_time_orders_counter()
        helper.create_order(user)
        assert int(order_page.get_all_time_orders_counter()) == int(old_counter) + 1


    @allure.title('Проверка счетчика "Выполнено за сегодня" в ленте заказов')
    @allure.description('Проверяем, что счетчик "Выполнено за сегодня" увеличивается после создания нового заказа.')
    def test_today_counter(self, driver, user):
        order_page = OrderList(driver)
        order_page.open_page(Urls.ORDER_LIST_PAGE)
        old_counter = order_page.get_today_orders_counter()
        helper.create_order(user)
        assert int(order_page.get_today_orders_counter()) == int(old_counter) + 1

    @allure.title('Проверка наличия заказа в разделе "В работе" в ленте заказов')
    @allure.description('Проверяем, что номер созданного заказа отображается в разделе "В работе" ленты заказов.')
    def test_word_in_progress(self, driver, user):
        order_page = OrderList(driver)
        order_page.open_page(Urls.ORDER_LIST_PAGE)
        response = helper.create_order(user)
        order_counter = response.json()['order']['number']
        assert str(order_counter) >= order_page.get_in_process_order_number()
