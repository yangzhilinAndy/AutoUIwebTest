#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import sys
from time import sleep
import pytest
from page.indexPage import Index
from utils.log import Log
from config import setting
from utils.GetYaml import getyaml

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


class TestIndex:
    """首页测试"""
    testDataPath = setting.TEST_DATA_YAML + "/index_data.yaml"
    reader = getyaml(testDataPath)
    log = Log()

    @pytest.fixture(scope='class')
    def po(self, driver):
        """
        所有测试方法的前置初始化，创建一个page实例
        """
        page = Index(driver)
        yield page

    @pytest.mark.parametrize("caseId, detail, screen, check1, check2", [reader.get_test_data(0)])
    def test_index_menu(self, po, caseId, detail, screen, check1, check2):
        """
        展开和回收全部讨论区菜单
        """
        self.log.info("执行测试用例ID-> {0} ; 测试点-> {1}".format(caseId, detail))
        assert po.click_menu_success_hint() == check1

        po.click_menu()  # 点击讨论区菜单，应当关闭
        assert po.click_menu_success_hint() == check2

        sleep(1)

        po.click_menu()  # 再次点击讨论区菜单，应当打开
        assert po.click_menu_success_hint() == check1
        po.get_screen_shot(screen)

    @pytest.mark.parametrize("caseId, detail, screen, inputData, check1", reader.get_multiple_test_data([1, 2, 3]))
    def test_index_search(self, po, caseId, detail, screen, inputData, check1):
        """
        在搜索框中输入关键词，看是否跳转到正确的搜索界面
        """
        self.log.info("执行测试用例ID-> {0} ; 测试点-> {1}".format(caseId, detail))
        po.search(inputData)
        assert po.search_success_hint() == check1
        po.get_screen_shot(screen)
        po.get_back_to_index()  # 回到首页

    @pytest.mark.parametrize("caseId, detail, screen", [reader.get_test_data(4)])
    def test_pictures(self, po, caseId, detail, screen):
        """
        检查首页轮播图与预览图是否一致
        """
        self.log.info("执行测试用例ID-> {0} ; 测试点-> {1}".format(caseId, detail))
        po.check_pictures()
        po.get_screen_shot(screen)
