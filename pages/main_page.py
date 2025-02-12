import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_list_page_locators import OrderListLocators
from selenium.webdriver import ActionChains


class MainPage(BasePage):
    @allure.step('Клик на кнопку "Конструктор" в хедере')
    def click_to_constructor_button(self):
        self.move_to_element_and_click(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Клик на кнопку "Лента Заказов" в хедере')
    def click_to_order_list_button(self):
        self.move_to_element_and_click(MainPageLocators.BUTTON_ORDER_LIST)

    @allure.step('Клик на первую булочку в списке ингредиентов')
    def click_to_ingredient(self):
        self.move_to_element_and_click(MainPageLocators.BUN_ID)

    @allure.step('Клик на кнопку "Закрыть" во всплывающем окне деталей ингредиента')
    def click_to_close_button_in_popup(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Проверка отображения окна "Детали ингредиента"')
    def check_ingredients_details(self):
        return self.availability_element(MainPageLocators.INGREDIENT_DETAILS).is_displayed()

    @allure.step('Ожидание исчезновения окна "Детали ингредиента"')
    def wait_for_order_details_disappear(self):
        self.wait_for_element_disappear(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_to_confirm_order_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_CONFIRMATION_BUTTON)


    @allure.step('Добавление первой булки в конструктор бургера')
    def add_ingredient_in_constructor(self):
        get_ingredient = self.find_element(MainPageLocators.BUN_ID)
        burger_area = self.find_element(MainPageLocators.BURGER_CONSTRUCTOR_AREA)

        moveing = ActionChains(self.driver)
        moveing.click_and_hold(get_ingredient).move_to_element(burger_area).release().perform()

    @allure.step('Поиск номера заказа во всплывающем окне подтверждения заказа')
    def get_order_confirm_number(self):
        self.find_element(MainPageLocators.ORDER_NUMBER_IN_COFIRMATION_POPUP)

    @allure.step('Получение текста кнопки "Войти в аккаунт"')
    def get_text_from_button_login(self):
        return self.get_text_from_element(MainPageLocators.BUTTON_LOGIN)

    @allure.step('Получение текста заголовка "Лента заказов"')
    def get_order_list_header(self):
        return self.get_text_from_element(OrderListLocators.ORDER_LIST_TEXT_HEADER)

    @allure.step('Получение текста заголовка окна "Детали ингредиента"')
    def get_details_from_ingredients(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Получение текста счетчика первого ингредиента')
    def get_number_from_ingredient_counter(self):
        return self.get_text_from_element(MainPageLocators.FIRST_INGREDIENT_COUNTER)

    @allure.step('Получение текста заголовка "идентификатор заказа" во всплывающем окне подтверждения заказа')
    def get_text_from_confirm_header(self):
        return self.get_text_from_element(MainPageLocators.ORDER_CONFIRMATION_HEADER)