#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver
import pytest
from config import setting
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help=""
    )

@pytest.fixture(scope="session")
def driver(pytestconfig):
    browser_name = pytestconfig.getoption("--browser")
    if browser_name == 'safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome(executable_path=setting.DRIVER_DIR+'/chromedriver')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
