#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException, NoSuchWindowException, NoAlertPresentException, \
    NoSuchElementException
import configparser
from utils.log import Log
from utils.screenshot import insert_img

con = configparser.ConfigParser()
# --------- 读取配置文件 ---------------
con.read(setting.CONFIG_PATH, encoding='utf-8')
log = Log()


class Page(object):
    """
    基础类，用于页面对象类的继承
    """

    def __init__(self, selenium_driver):
        self.base_url = con.get("WebURL", "URL")
        self.driver = selenium_driver
        self.timeout = con.getint("Driver", "Timeout")

    def open(self, url):
        """
        打开浏览器URL访问
        :param url: URL地址
        :return:
        """
        url = self.base_url + url
        self.driver.get(url)


    def find_element(self, *loc):
        """
        单个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            log.error("{0}页面中未能找到{1}元素".format(self, loc))

    def find_elements(self, *loc):
        """
        多个元素定位
        :param loc: 传入元素属性
        :return: 定位到的元素
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            log.error("{0}页面中未能找到{1}元素".format(self, loc))

    def script(self, src):
        """
        提供调用JavaScript方法
        :param src: 脚本文件
        :return: JavaScript脚本
        """
        return self.driver.execute_script(src)

    def switch_frame(self, loc):
        """
        多表单嵌套切换
        :param loc: 传元素的属性值
        :return: 定位到的元素
        """
        try:
            return self.driver.switch_to_frame(loc)
        except NoSuchFrameException as msg:
            log.error("查找iframe异常-> {0}".format(msg))

    def switch_windows(self, loc):
        """
        多窗口切换
        :param loc:
        :return:
        """
        try:
            return self.driver.switch_to_window(loc)
        except NoSuchWindowException as msg:
            log.error("查找窗口句柄handle异常-> {0}".format(msg))

    def switch_alert(self):
        """
        警告框处理
        :return:
        """
        try:
            return self.driver.switch_to_alert()
        except NoAlertPresentException as msg:
            log.error("查找alert弹出框异常-> {0}".format(msg))

    def get_screen_shot(self, file_name):
        insert_img(self.driver, file_name)

