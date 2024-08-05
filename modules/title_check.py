from selene import browser, have
import allure


class GismeteoTitleCheck:

    def open(self, address=''):
        with allure.step('Открываем сайт gismeteo'):
            browser.open(address)

    def moscow_choise(self):
        with allure.step('Выбираем "Москву"'):
            browser.element('[placeholder="Поиск местоположения"]').type('Москва')
            browser.element('[href="/weather-moscow-4368/"]').click()

    def gismeteo_title_check_on_app_page(self):
        with allure.step('Проверяем Title страницы'):
            browser.should(have.title('GISMETEO'))


    def today_weather_title_check(self):
        with allure.step('Проверяем наименование."Погода в Москве сегодня"'):
            browser.element('.page-title').should(have.text('Погода в Москве сегодня'))

    def three_days_weather_title_check(self):
        with allure.step('Проверяем наименование."Погода в Москве на 3 дня"'):
            browser.element('[data-stat-value="3-days"]').click()
            browser.element('.page-title').should(have.text('Погода в Москве на 3 дня'))

    def radar_title_check(self):
        with allure.step('Проверяем наименование."Радар осадков и гроз в Москве"'):
            browser.element('[href="/nowcast-moscow-4368/"]').click()
            browser.element('.page-title').should(have.text('Радар осадков и гроз в Москве'))

    def open_moscow(self):
        with allure.step('Ищем город "Москва" через поиск'):
            self.open()
            self.moscow_choise()


    def open_moscow_check(self):
        with allure.step('Ищем город "Москва" через поиск'):
            browser.all('.breadcrumbs-link').second.should(have.text('Москва (город федерального значения)'))

gismeteo_action = GismeteoTitleCheck()
