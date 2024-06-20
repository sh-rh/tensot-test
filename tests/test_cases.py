from tests.pages.sbistensorpages import SbisPage


def test_first_case(chrome):
    """  
    Реализация первого сценария:
    1) Перейти на https://sbis.ru/ в раздел "Контакты"
    2) Найти баннер Тензор, кликнуть по нему
    3) Перейти на https://tensor.ru/
    4) Проверить, что есть блок "Сила в людях"
    5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    6) Находим раздел Работаем и проверяем, что у всех фотографии хронологии одинаковые высота (height) и ширина (width)
    """
    page = SbisPage(chrome)

    page.go_to_site()
    page.click_contacts()
    page.click_tensor_banner()
    page.switch_window_close_origin()
    page.validate_block_mans_power()
    page.about_link_click()
    page.validate_about_link_click()
    page.find_working_block
    page.validate_image_size()


def test_second_case(chrome):
    """
    Реализация второго сценария:
    1) Перейти на https://sbis.ru/ в раздел "Контакты"
    2) Проверить, что определился ваш регион (в нашем примере Ярославская обл.) и есть список партнеров.
    3) Изменить регион на Камчатский край
    4) Проверить, что подставился выбранный регион, список партнеров изменился, url и title содержат информацию выбранного региона
    """
    page = SbisPage(chrome)

    page.go_to_site()
    page.click_contacts()
    page.validate_region_chooser()
    page.is_list_partners()
    page.change_region()
    page.validate_change_region()
