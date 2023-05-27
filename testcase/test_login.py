#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pytest
from public.models import screenshot
from public.models.excelHelper import read_excel
from public.page_obj.loginPage import login
from public.models.log import Log


class TestLogin:
    """首页登录测试"""
    filePath = "../testdata/login_data.xlsx"

    @pytest.mark.parametrize("caseId, detail, username, password, screen, check", read_excel(filePath))
    def test_login(self, driver, caseId, detail, username, password, screen, check):
        """
        登录测试
        """
        log = Log()
        log.info("执行测试用例ID: {0} ; 测试点: {1} ".format(caseId, detail))
        # 调用登录方法
        login(driver).user_login(username, password)
        po = login(driver)
        # 判断是正向还是反向用例
        if screen == 'login_success':
            log.info("检查点-> {0}".format(po.user_login_success_hint()))
            assert po.user_login_success_hint() == check
            log.info("成功登录，返回结果是: {0}".format(po.user_login_success_hint()))
            screenshot.insert_img(driver, screen + '.jpg')
            log.info("-----> 开始执行退出流程操作")
            login(driver).login_exit()
            po_exit = login(driver)
            log.info("检查点-> 找到{0}元素,表示退出成功！".format(po_exit.exit_login_success_hint()))
            assert po_exit.exit_login_success_hint() == '账号'
            log.info("退出登录，返回实际结果是: {0}".format(po_exit.exit_login_success_hint()))
        else:
            log.info("检查点-> {0}".format(po.login_error_hint()))
            assert po.login_error_hint() == check
            log.info("异常登录，返回实际结果是->: {0}".format(po.login_error_hint()))
            screenshot.insert_img(driver, screen + '.jpg')


