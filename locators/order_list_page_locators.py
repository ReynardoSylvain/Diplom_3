from selenium.webdriver.common.by import By

class OrderListLocators:
    ORDER_LIST_TEXT_HEADER = By.XPATH, '//h1[contains(text(),"Лента заказов")]'
    FIRST_ORDER_IN_LIST = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    ORDER_DETAILS_HEADER = By.XPATH, '//p[text()="Cостав"]'
    ORDERS_LIST_BY_NUMBER = By.XPATH, '//*[text()="#0{num_order}"]'
    ALL_ORDERS_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "digits-large")]')
    TODAY_ORDERS_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "digits-large")]')
    ORDERS_IN_PROCESS = By.XPATH, '//*[contains(@class, "orderListReady")]//li[contains(@class, "digits-default")]'
    READY_FOR_ALL_ORDERS = By.XPATH, '//li[@class="text text_type_main-small"]'
