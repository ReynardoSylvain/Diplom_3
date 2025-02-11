from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    RECOVER_PASSWORD_BUTTON = By.XPATH, '//a[contains(text(),"Восстановить пароль")]'
    RECOVER_BUTTON = By.XPATH, '//button[contains(text(),"Восстановить")]'
    EMAIL_INPUT_FIELD = By.XPATH, '//input[@name="name"]'
    PASSWORD_RECOVERY_PAGE_HEADER = By.XPATH, '//h2[contains(text(),"Восстановление пароля")]'
    SHOW_PASSWORD_VISIBILITY_BUTTON = By.XPATH, '//div[@class="input__icon input__icon-action"]'
    PASSWORD_INPUT_FIELD_ACTIVE_FRAME = By.XPATH, '//div[contains(@class, "input_status_active")]'
