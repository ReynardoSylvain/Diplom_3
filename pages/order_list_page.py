import allure
from pages.base_page import BasePage
from locators.order_list_page_locators import OrderListLocators
from locators.profile_page_locators import ProfilePageLocators


class OrderList(BasePage):

    @allure.step('Клик на первый заказ в списке заказов')
    def click_on_order(self):
        self.click_to_element(OrderListLocators.FIRST_ORDER_IN_LIST)

    @allure.step('Поиск заказа в списке заказов по номеру')
    def search_element_by_order_number(self, num_order):
        num_order_text = OrderListLocators.ORDERS_LIST_BY_NUMBER
        num_order_text = (num_order_text[0], num_order_text[1].format(num_order=num_order))
        return self.find_element(num_order_text)

    @allure.step('Получение количества заказов "Выполнено за все время"')
    def get_all_time_orders_counter(self):
        return self.get_text_from_element(OrderListLocators.ALL_ORDERS_COUNTER)

    @allure.step('Получение количества заказов "Выполнено за сегодня"')
    def get_today_orders_counter(self):
        return self.get_text_from_element(OrderListLocators.TODAY_ORDERS_COUNTER)

    @allure.step('Получение номера первого заказа в списке "В работе"')
    def get_in_process_order_number(self):
        return self.get_text_from_element(OrderListLocators.ORDERS_IN_PROCESS)

    @allure.step('Получение текста заголовка попапа "Состав заказа"')
    def get_text_from_details(self):
        return self.get_text_from_element(OrderListLocators.ORDER_DETAILS_HEADER)

    @allure.step('Получение номера заказа из истории заказов в личном кабинете')
    def get_order_number(self):
        return self.get_text_from_element(ProfilePageLocators.ORDER_NUMBER_IN_HISTORY)
