#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from page.base import Page
from time import sleep
from utils.GetYaml import getyaml
from selenium.webdriver.support.select import Select

testData = getyaml(setting.TEST_Element_YAML + '/' + 'login.yaml')


class login(Page):
    """
    用户登录页面
    """
    url = '/'

    # username输入框
    login_username_loc = Page.get_element_from_data(1, testData)
    # 密码输入框
    login_password_loc = Page.get_element_from_data(2, testData)
    # 取消自动登录
    keep_login_button_loc = Page.get_element_from_data(3, testData)
    # 单击登录
    login_user_loc = Page.get_element_from_data(4, testData)
    # 单击验证框
    login_verify_loc = Page.get_element_from_data(5, testData)
    # 选择退出
    login_exit_button_loc = Page.get_element_from_data(6, testData)

    def keep_login(self):
        """
        取消自动登录
        :return:
        """

        select = self.find_element(*self.keep_login_button_loc)
        Select(select).select_by_value("0")

    def login_exit(self):
        """
        退出系统
        :return:
        """
        self.find_element(*self.login_exit_button_loc).click()

    def user_login(self, username, password):
        """
        登录入口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.open(self.url)
        self.find_element(*self.login_username_loc).send_keys(username)
        self.find_element(*self.login_password_loc).send_keys(password)
        self.keep_login()
        sleep(1)
        self.find_element(*self.login_user_loc).click()
        sleep(1)
        self.find_element(*self.login_verify_loc).click()
        sleep(1)

    error_hint_loc = Page.get_check_from_data(0, testData)
    user_login_success_loc = Page.get_check_from_data(1, testData)
    exit_login_success_loc = Page.get_check_from_data(2, testData)

    # 手机号或密码错误提示
    def login_error_hint(self):
        return self.find_element(*self.error_hint_loc)

    # 登录成功用户名
    def user_login_success_hint(self):
        return self.find_element(*self.user_login_success_loc)

    # 退出登录
    def exit_login_success_hint(self):
        return self.find_element(*self.exit_login_success_loc)
