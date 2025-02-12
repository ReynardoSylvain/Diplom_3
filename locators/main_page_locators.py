from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_ACCOUNT = By.XPATH, '//p[contains(text(),"Личный Кабинет")]'
    BUTTON_CONSTRUCTOR = By.XPATH, '//p[contains(text(),"Конструктор")]'
    BUTTON_ORDER_LIST = By.XPATH, '//p[contains(text(),"Лента Заказов")]'
    BUTTON_LOGIN = By.XPATH, '//button[contains(text(),"Войти в аккаунт")]'

    BUN_ID = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    INGREDIENT_DETAILS = By.XPATH, '//h2[contains(text(),"Детали ингредиента")]'
    CLOSE_INGREDIENT_DETAILS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
    BURGER_CONSTRUCTOR_AREA = By.XPATH, '//*[@class="BurgerConstructor_basket__list__l9dp_"]'
    TOPPINGS_BUTTON = By.XPATH, '//span[contains(text(),"Начинки")]'

    FIRST_INGREDIENT_COUNTER = (By.XPATH, "//ul[1]/a[1]//p[contains(@class, 'num')]")

    ORDER_CONFIRMATION_BUTTON = By.XPATH, '//button[contains(text(),"Оформить заказ")]'
    ORDER_CONFIRMATION_HEADER = By.XPATH, '//p[@class="undefined text text_type_main-medium mb-15"]'
    ORDER_NUMBER_IN_COFIRMATION_POPUP = By.XPATH, '//*[contains(@class, "type_digits-large")]'
