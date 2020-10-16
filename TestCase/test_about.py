#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
import pytest
import allure
from tools.logger import log
from common.readconfig import ini
from page_object.aboutpage import AboutPage


@allure.feature("测试About页面")
class TestAbout:
    @allure.story("打开codechina")
    @pytest.fixture(scope='function', autouse=True)
    def test_opencodechina(self, drivers):
        """打开codechina"""
        search = AboutPage(drivers)
        search.get_url(ini.url)

    @allure.story("检查页面")
    def test_checkpage(self, drivers):
        """搜索"""
        search = AboutPage(drivers)
        search.input_search("selenium")
        search.click_search()
        result = re.search(r'selenium', search.get_source)
        log.info(result)
        assert result


if __name__ == '__main__':
    pytest.main(['TestCase/test_search.py', '--alluredir', './report/allure'])
    os.system('allure serve report/allure')
    #pytest.main(['TestCase/test_search.py'])