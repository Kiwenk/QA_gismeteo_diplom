import allure
from modules.title_check import GismeteoTitleCheck

gismeteo_action = GismeteoTitleCheck()

@allure.feature('Базовый UI')
@allure.story('Пользователь смотрит тайтл на странице "Приложения"')
@allure.link('https://www.gismeteo.ru/soft/')
@allure.description('Проверка наименования страницы')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.NORMAL)
def test_check_title_on_app_page():
    with allure.step('Открываем раздел "Приложения" на сайте gismeteo'):
        gismeteo_action.open('soft/')

    with allure.step('Проверяем Title страницы'):
        gismeteo_action.gismeteo_title_check_on_app_page()

@allure.feature('Поиск города')
@allure.story("Пользователь ищет город 'Москва'")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка работоспособности поиска')
@allure.label('gismeteo_search_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_check():
    with allure.step('Проверяем работоспособность поиска. Город "Москва"'):
        gismeteo_action.open_moscow()

@allure.feature('Базовый UI')
@allure.story("Пользователь смотрит погоду в Москве на сегодня")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.MINOR)
def test_check_today_weather_title():
    with allure.step('Находим "Москву"'):
        gismeteo_action.open_moscow()

    with allure.step('Проверяем наименование."Погода в Москве сегодня"'):
        gismeteo_action.today_weather_title_check()

@allure.feature('Базовый UI')
@allure.story("Пользователь смотрит погоду в Москве на 3 дня")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.MINOR)
def test_check_3_days_weather_title():
    with allure.step('Находим "Москву"'):
        gismeteo_action.open_moscow()

    with allure.step('Проверяем наименование."Погода в Москве на 3 дня"'):
        gismeteo_action.three_days_weather_title_check()

@allure.feature('Базовый UI')
@allure.story("Пользователь радар по Москве")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.NORMAL)
def test_check_radar():
    with allure.step('Находим "Москву"'):
        gismeteo_action.open_moscow()

    with allure.step('Проверяем наименование."Радар осадков и гроз в Москве"'):
        gismeteo_action.radar_title_check()
