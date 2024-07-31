from selene import browser, have


class GismeteoTitleCheck:

    def open(self, address = ''):
        browser.open(address)

    def moscow_choise(self):
        browser.element('[placeholder="Поиск местоположения"]').type('Москва')
        browser.element('[href="/weather-moscow-4368/"]').click()

    def gismeteo_title_check_on_app_page(self):
        browser.should(have.title('GISMETEO'))

    def today_weather_title_check(self):
        browser.element('.page-title').should(have.text('Погода в Москве сегодня'))

    def three_days_weather_title_check(self):
        browser.element('[data-stat-value="3-days"]').click()
        browser.element('.page-title').should(have.text('Погода в Москве на 3 дня'))

    def radar_title_check(self):
        browser.element('[href="/nowcast-moscow-4368/"]').click()
        browser.element('.page-title').should(have.text('Радар осадков и гроз в Москве'))

    def open_moscow(self):
        self.open()
        self.moscow_choise()


