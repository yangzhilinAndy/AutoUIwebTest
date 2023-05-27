#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import sys
from time import sleep
import pytest
from page.indexPage import Index
from utils.log import Log
from config import setting
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class TestIndex:
    """首页测试"""
    testDataPath = setting.TEST_DATA_YAML + "/index_data.yaml"

    @pytest.fixture(scope='class')
    def po(self, driver):
        """
        所有测试方法的前置初始化，创建一个page实例
        """
        page = Index(driver)
        yield page

    def test_pictures(self, po):
        po.check_pictures()

    @pytest.mark.parametrize("caseId, detail, screen, check1, check2", [next(excel_file)])
    def test_index_menu(self, po, caseId, detail, screen, check1, check2):
        """
        首页测试
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(caseId, detail))
        assert po.click_menu_success_hint() == check1
        po.click_menu()
        assert po.click_menu_success_hint() == check2
        log.info("返回实际结果是->: {0}".format(po.click_menu_success_hint()))
        sleep(3)

        po.click_menu()
        assert po.click_menu_success_hint() == check1
        log.info("返回实际结果是->: {0}".format(po.click_menu_success_hint()))

    @pytest.mark.parametrize("caseId, detail, screen, check1, check2", [next(excel_file)])
    def test_index_search(self, po, caseId, detail, screen, check1, check2):
        po.search('abc')
        assert po.search_success_hint() == check1
        assert po.search_success_hint2() == check2

