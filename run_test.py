#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import sys

sys.path.append(os.path.dirname(__file__))
from config import setting
import pytest


def run_cases(browser_name, testcases_path):
    """执行所有的测试用例"""
    allure_temp_results = f'{setting.TEST_RESULT}/temp'
    allure_report_path = f'{setting.TEST_RESULT}/html_report'
    pytest.main(
        ['--browser=' + browser_name, '-v', testcases_path, '-s', f'--alluredir={allure_temp_results}',
         '--clean-alluredir'])

    os.system(f"allure generate {allure_temp_results} -o {allure_report_path} --clean")


if __name__ == "__main__":
    browser = 'chrome'
    testcases = setting.TEST_DIR + '/test_index.py'

#    run_cases(browser, testcases)
