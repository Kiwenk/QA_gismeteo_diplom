import allure
import pytest

from pages.ui_check_methods import gismeteo_ui_action


@allure.feature('Базовый UI')
@allure.story('Пользователь смотрит тайтл на странице "Приложения"')
@allure.link('https://www.gismeteo.ru/soft/')
@allure.description('Проверка наименования страницы')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.NORMAL)
def test_check_title_on_app_page():
    gismeteo_ui_action.open('soft/')
    gismeteo_ui_action.gismeteo_title_check_on_app_page()


@allure.feature('Поиск города')
@allure.story("Пользователь ищет город 'Москва'")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка работоспособности поиска')
@allure.label('gismeteo_search_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_check():
    gismeteo_ui_action.open_moscow()
    gismeteo_ui_action.open_moscow_check()


@allure.feature('Базовый UI')
@allure.story("Пользователь смотрит погоду в Москве на сегодня")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.MINOR)
def test_check_today_weather_title():
    gismeteo_ui_action.open_moscow()
    gismeteo_ui_action.today_weather_title_check()


@allure.feature('Базовый UI')
@allure.story("Пользователь смотрит погоду в Москве на 3 дня")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.MINOR)
def test_check_3_days_weather_title():
    gismeteo_ui_action.open_moscow()
    gismeteo_ui_action.three_days_weather_title_check()


@allure.feature('Базовый UI')
@allure.story("Пользователь радар по Москве")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.NORMAL)
def test_check_radar():
    gismeteo_ui_action.open_moscow()
    gismeteo_ui_action.radar_title_check()


@allure.feature('Базовый UI')
@allure.story("Пользователь радар по Москве")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.MINOR)
def test_nav_buttons():
    gismeteo_ui_action.open('/')
    gismeteo_ui_action.nav_buttons_is_visible()


@allure.feature('Базовый UI')
@allure.story("Пользователь радар по Москве")
@allure.link('https://www.gismeteo.ru/')
@allure.description('Проверка корректности наименования')
@allure.label('gismeteo_UI_check')
@allure.tag('gismeteo_UI')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize('text', ['Сейчас', 'Сегодня', 'Завтра', '3 дня', '10 дней', '2 недели', 'Месяц', 'Радар'])
def test_nav_text(text):
    gismeteo_ui_action.open('/')
    gismeteo_ui_action.nav_text_is_visible(text)
