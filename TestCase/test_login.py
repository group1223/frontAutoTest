#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
import pytest
import allure
from tools.times import sleep
from tools.logger import log
from common.readconfig import ini
from page_object.loginpage import LoginPage



@allure.feature("登录")
class TestLogin:
    """测试登录"""

    @allure.story("登录codechina")
    @pytest.fixture(scope='function', autouse=True)
    def open_codechina(self, drivers):
        """打开codechina"""
        login_in = LoginPage(drivers)
        login_in.get_url(ini.url)


    @allure.story("登录")
    @pytest.mark.smoke
    @allure.severity("critical")
    @pytest.mark.parametrize("name,pwd", [('cpongo5', 'abc123')])
    def test_login(self, drivers, name, pwd):
        login = LoginPage(drivers)
        login.loginIn()
        login.username(name)
        login.password(pwd)
        login.submit()
        sleep(3)
        log.info('登录成功')
        # res = login.alert_exists()
        # if res:
        #     assert res == "登录失败，请检查您的用户名或密码是否填写正确。"
        # elif login.login_success():
        #     login.quit_login()



if __name__ == '__main__':
    pytest.main(['TestCase/test_login.py', '--alluredir', './report/allure'])
    os.system('allure serve report/allure')
    #pytest.main(['TestCase/test_login.py'])
