import allure
from modules.title_check import gismeteo_action


@allure.feature('Базовый UI')
@allure.story('Пользователь смотрит тайтл на странице "Приложения"')
@allure.link('https://www.gismeteo.ru/soft/')
@allure.description('Проверка наименования страницы')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.NORMAL)
def test_check_title_on_app_page():
    gismeteo_action.open('soft/')
    gismeteo_action.gismeteo_title_check_on_app_page()


@allure.feature('Поиск города')
@allure.story("Пользователь ищет город 'Москва'")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка работоспособности поиска')
@allure.label('gismeteo_search_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_check():
    gismeteo_action.open_moscow_check()


@allure.feature('Базовый UI')
@allure.story("Пользователь смотрит погоду в Москве на сегодня")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.MINOR)
def test_check_today_weather_title():
    gismeteo_action.open_moscow()
    gismeteo_action.today_weather_title_check()


@allure.feature('Базовый UI')
@allure.story("Пользователь смотрит погоду в Москве на 3 дня")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.MINOR)
def test_check_3_days_weather_title():
    gismeteo_action.open_moscow()
    gismeteo_action.three_days_weather_title_check()


@allure.feature('Базовый UI')
@allure.story("Пользователь радар по Москве")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.NORMAL)
def test_check_radar():
    gismeteo_action.open_moscow()
    gismeteo_action.radar_title_check()
