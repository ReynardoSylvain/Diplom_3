from selenium.webdriver.common.by import By

class ProfilePageLocators:
    EMAIL_INPUT_FIELD = By.XPATH, '//input[@name="name"]'
    PASSWORD_INPUT_FIELD = By.XPATH, '//input[@name="Пароль"]'
    LOGIN_BUTTON = By.XPATH, '//button[contains(text(),"Войти")]'
    ORDER_HISTORY_BUTTON = By.XPATH, '//a[contains(text(),"История заказов")]'
    EXIT_BUTTON = By.XPATH, '//button[contains(text(),"Выход")]'
    ORDER_NUMBER_IN_HISTORY = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'
