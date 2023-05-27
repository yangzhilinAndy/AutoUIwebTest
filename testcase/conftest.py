#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver
import pytest

def pytest_addoption(parser):
    """
    pytest_addoption 可以让用户注册一个自定义的命令行参数，方便用户将数据传递给 pytest；
    这个 Hook 方法一般和 内置 fixture pytestconfig 配合使用，pytest_addoption 注册命令行参数，
    pytestconfig 通过配置对象读取参数的值；
    :param parser:
    :return:
    """
    parser.addoption(
        "--browser", action="store", default="chrome", help=""
    )

@pytest.fixture(scope="session")
def driver(pytestconfig):
    browser_name = pytestconfig.getoption("--browser")
    path = '../driver/chromedriver'
    if browser_name == 'safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome(executable_path=path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
