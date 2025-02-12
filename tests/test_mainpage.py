import allure
from data import Urls
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.main_page_locators import MainPageLocators


@allure.story('Главная страница и функционал конструктора')

class TestMainpageAndConstruktor:

    @allure.title('Переход по кнопке "Конструктор" на главной странице')
    @allure.description('Проверяем, что при нажатии на кнопку "Конструктор" происходит переход на главную страницу.')
    def test_opening_constructor(self, driver):
        homepage = MainPage(driver)
        homepage.open_page(Urls.ORDER_LIST_PAGE)
        homepage.click_to_constructor_button()
        assert (homepage.get_current_url() == Urls.BASE_PAGE and
                homepage.get_text_from_button_login() == 'Войти в аккаунт')

    @allure.title('Переход по кнопке "Лента Заказов" на главной странице')
    @allure.description('Проверяем, что при нажатии на кнопку "Лента Заказов" происходит переход на страницу ленты заказов.')
    def test_opening_order_list(self, driver):
        homepage = MainPage(driver)
        homepage.open_page(Urls.BASE_PAGE)
        homepage.click_to_order_list_button()
        assert (homepage.get_current_url() == Urls.ORDER_LIST_PAGE and
                homepage.get_order_list_header() == 'Лента заказов')

    @allure.title('Открытие всплывающего окна с деталями ингредиента')
    @allure.description('Проверяем, что при клике на ингредиент открывается всплывающее окно "Детали ингредиента".')
    def test_ingredient_details(self, driver):
        homepage = MainPage(driver)
        homepage.open_page(Urls.BASE_PAGE)
        homepage.click_to_ingredient()
        assert homepage.get_details_from_ingredients() == 'Детали ингредиента'

    @allure.title('Закрытие всплывающего окна ингредиента по кнопке "Закрыть"')
    @allure.description('Проверяем, что при нажатии на кнопку "Закрыть" во всплывающем окне ингредиента, окно закрывается.')
    def test_ingredient_details_close_button(self, driver):
        homepage = MainPage(driver)
        homepage.open_page(Urls.BASE_PAGE)
        homepage.click_to_ingredient()
        homepage.click_to_close_button_in_popup()
        homepage.wait_for_order_details_disappear()
        assert homepage.check_ingredients_details() == False


    @allure.title('Увеличение счетчика ингредиентов при добавлении в конструктор')
    @allure.description('Проверяем, что счетчик ингредиентов увеличивается при перетаскивании ингредиента в конструктор (по умолчанию 0 в конструкторе).')
    def test_ingredient_counter(self, driver):
        homepage = MainPage(driver)
        homepage.open_page(Urls.BASE_PAGE)
        homepage.add_ingredient_in_constructor()
        assert homepage.get_number_from_ingredient_counter() != '0'
        #Тест счетчика ингредиентов не работает в Файрфоксе ни через drag and drop ни через ActionChains

    @allure.title('Успешное оформление заказа авторизованным пользователем')
    @allure.description('Проверяем, что авторизованный пользователь может оформить заказ, и появляется окно с номером заказа и текстом "идентификатор заказа".')
    def test_placing_order_by_authorized_user(self, driver, user):
        homepage = MainPage(driver)
        profile_page = ProfilePage(driver)
        homepage.open_page(Urls.LOGIN_PAGE)
        profile_page.login(user)
        homepage.wait_url_change(Urls.BASE_PAGE)
        homepage.add_ingredient_in_constructor()
        homepage.click_to_confirm_order_button()
        homepage.get_order_confirm_number()
        assert homepage.get_text_from_confirm_header() == 'идентификатор заказа'

