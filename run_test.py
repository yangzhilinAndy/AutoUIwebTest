#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os,sys
sys.path.append(os.path.dirname(__file__))
from config import setting
import pytest, threading
from public.models.sendmail import send_mail

testcases = setting.TEST_DIR + '/test_index.py'

def runner(name):
    pytest.main(['--browser='+name, '-v', testcases, '-s', f'--alluredir={setting.TEST_RESULT}/temp_json_report_'+name, '--clean-alluredir'])

def run_cases(browser_list):
    """执行所有的测试用例,
    如果有多个browser,启动多线程执行"""
    thread_list = []
    for b in browser_list:
        thread = threading.Thread(target=runner, args=(b,))
        thread_list.append(thread)
    for j in thread_list:
        j.start()
    for t in thread_list:
        t.join()
    for b in browser_list:
        os.system(f"allure generate {setting.TEST_RESULT}/temp_json_report_{b} -o {setting.TEST_RESULT}/html_{b}_report --clean")
  #  send_mail(report) #调用发送邮件模块

if __name__ =="__main__":
    browser_list = ('chrome','safari')
    os.environ['PATH'] += "/Users/zhilinyang/Desktop/webTest/allure-2.22.1/bin:"
    run_cases(browser_list)
