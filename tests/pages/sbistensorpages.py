from selenium.webdriver.common.by import By
import time

from tests.pages.basepage import BasePage


class SbisPage(BasePage):

    # Переменные для первого кейса.

    locator_sbis_contacts = (By.LINK_TEXT, 'Контакты')
    locator_sbis_tensores_baner = (
        By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
    locator_tensor_mans_power_block = (
        By.CLASS_NAME, 'tensor_ru-Index__block4')
    locator_tensor_about_link = (
        By.CSS_SELECTOR, 'div.tensor_ru-Index__block4 a')
    locator_tensor_working_block = (By.CLASS_NAME, 'tensor_ru-About__block3')
    locator_tensor_working_images = (
        By.CSS_SELECTOR, 'div.tensor_ru-About__block3 img')
    tensor_about_url = 'https://tensor.ru/about'

    # Переменные для второго кейса.

    locator_sbis_region_chooser = (
        By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    locator_sbis_contacts_container_items = (
        By.CSS_SELECTOR, 'div[name="itemsContainer"] div[data-qa="item"]')
    my_region = 'Новосибирская обл.'
    new_region = 'Камчатский край'
    locator_sbis_new_region = (By.CSS_SELECTOR, f'span[title="{new_region}"]')
    new_region_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    new_region_title = 'СБИС Контакты — Камчатский край'
    partner_new_list = 'СБИС - Камчатка'
    
    # Функции для первого кейса.

    def click_contacts(self):
        contacts_link = self.find_element(self.locator_sbis_contacts)
        contacts_link.click()
        return contacts_link

    def click_tensor_banner(self):
        tensor_banner = self.find_element(
            self.locator_sbis_tensores_baner)
        tensor_banner.click()
        return tensor_banner

    def find_block_mans_power(self):
        return self.find_element(self.locator_tensor_mans_power_block)

    def validate_block_mans_power(self):
        block_text = self.find_block_mans_power().text

        assert 'Сила в людях' in block_text

    def about_link_click(self):
        about_link = self.find_element(self.locator_tensor_about_link)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", about_link)
        about_link.click()

    def validate_about_link_click(self):
        assert self.driver.current_url == self.tensor_about_url

    def find_working_block(self):
        self.find_element(self.locator_tensor_working_block)

    def validate_image_size(self):
        images = self.find_elements(self.locator_tensor_working_images)

        images_height_and_width = set()

        for image in images:
            images_height_and_width.update(list(image.size.values()))

        assert len(images_height_and_width) == 2

    # Функции для второго кейса.

    def find_region_chooser(self):
        return self.find_element(self.locator_sbis_region_chooser)

    def validate_region_chooser(self, validated_region: str = my_region):
        current_region = self.find_region_chooser()

        try:
            assert validated_region in current_region.text

        except AssertionError:
            print(f'Не {self.my_region} :(')

    def is_list_partners(self):
        contacts = self.find_elements(
            self.locator_sbis_contacts_container_items)

        assert len(contacts) > 1

    def change_region(self):
        region_chooser = self.find_region_chooser()
        region_chooser.click()

        new_region = self.find_element(self.locator_sbis_new_region)
        new_region.click()
        time.sleep(3)

        current_region = self.find_region_chooser()

        assert self.new_region in current_region.text

    def validate_change_region(self):
        assert self.driver.current_url == self.new_region_url
        assert self.driver.title == self.new_region_title
        contacts = self.find_elements(
            self.locator_sbis_contacts_container_items)
        
        contacts_texts = []
        
        for contact in contacts:
            contacts_texts.append(contact.text)
            
        texts = ' '.join(contacts_texts)
        assert self.partner_new_list in texts