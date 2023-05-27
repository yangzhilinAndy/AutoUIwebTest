#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

os.environ['PATH'] += (BASE_DIR + "/allure-2.22.1/bin:")

# 驱动的路径
DRIVER_DIR = os.path.join(BASE_DIR, 'driver')
# 测试网站配置文件
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "test_web.ini")
# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR, "testcase")

# 日志目录
LOG_DIR = os.path.join(BASE_DIR, "logs")
# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR, "testdata")
# 元素控件
TEST_Element_YAML = os.path.join(BASE_DIR, "testElement")

# 测试结果
TEST_RESULT = os.path.join(BASE_DIR, "result")
