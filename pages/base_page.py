import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие URL в браузере')
    def open_page(self, url):
        return self.driver.get(url)

    @allure.step('Получение текущего URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание изменения URL страницы')
    def wait_url_change(self, url, time=10):
        return WebDriverWait(self.driver, time).until(ec.url_to_be(url))

    @allure.step('Ожидание исчезновения элемента')
    def wait_for_element_disappear(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.invisibility_of_element(locator))

    @allure.step('Поиск видимого элемента на странице')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator))

    @allure.step('Проверка присутствия элемента')
    def availability_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).text

    @allure.step('Клик по элементу')
    def click_to_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator)).click()

    @allure.step('Перемещение к элементу и клик')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        moveing = ac(self.driver)
        moveing.move_to_element(element).click().perform()

    @allure.step('Ввод текста в поле ввода')
    def enter_data(self, locator, data, time=10):
        WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).send_keys(data)

    @allure.step('Перетаскивание элемента в цель')
    def drag_and_drop(self, element, target):
        return ac(self.driver).drag_and_drop(element, target).perform()
