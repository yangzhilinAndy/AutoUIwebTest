#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium.webdriver.common.keys import Keys
import os, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from page.basePage import Page
from time import sleep
from utils.GetYaml import getyaml


class Index(Page):
    url = '/nForum/#!mainpage'
    elementData = getyaml(setting.TEST_Element_YAML + '/' + 'index.yaml')

    def __init__(self, driver):
        super().__init__(driver)
        self.open(self.url)
        self.left_menu_button = self.elementData.get_element_from_data(0)
        self.menu_success_hint = self.elementData.get_check_from_data(0)
        self.search_box = self.elementData.get_element_from_data(1)
        self.menu_success_hint2 = self.elementData.get_check_from_data(1)
        self.pictures = self.elementData.get_element_from_data(2)
        self.previews = self.elementData.get_element_from_data(3)
        self.results = self.elementData.get_element_from_data(4)

    def click_menu(self):
        """
         点击菜单
        """
        WebDriverWait(self.driver, 3, 0.5).until(
            expected_conditions.element_to_be_clickable(self.left_menu_button)
        )
        self.find_element(*self.left_menu_button).click()
        sleep(2)

    def click_menu_success_hint(self):
        return self.find_element(*self.menu_success_hint).get_attribute("class")

    def search(self, keyword):
        WebDriverWait(self.driver, 3, 0.5).until(
            expected_conditions.presence_of_element_located(self.search_box)
        )
        self.find_element(*self.search_box).clear()
        sleep(1)
        self.find_element(*self.search_box).send_keys(keyword)
        sleep(1)
        self.find_element(*self.search_box).send_keys(Keys.ENTER)
        sleep(1)

    def get_back_to_index(self):
        self.open(self.url)

    def search_success_hint(self):
        return self.driver.current_url

    def search_success_hint2(self):
        return self.find_element(*self.menu_success_hint2).text

    def check_pictures(self):
        links = self.find_element(*self.pictures).find_elements(By.XPATH, './a')
        preview_list = self.find_element(*self.previews)
        for link in links:
            WebDriverWait(self.driver, 10, 0.5).until(
                expected_conditions.visibility_of(link)
            )
            p = preview_list.find_element(By.XPATH, './a[@class="cur"]')
            assert link.get_attribute("href") == p.get_attribute("href")

    def get_search_results(self):
        return self.find_element(*self.results).find_elements(By.XPATH, './tr')

