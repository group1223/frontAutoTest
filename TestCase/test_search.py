#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
import pytest
import allure
from tools.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage


@allure.feature("测试百度模块")
class TestSearch:
    #@allure.story("打开codechina")
    @pytest.fixture(scope='function', autouse=True)
    def open_codechina(self, drivers):
        """打开codechina"""
        search = SearchPage(drivers)
        search.get_url(ini.url)

    # @allure.story("搜索selenium结果用例")
    # def test_001(self, drivers):
    #     """搜索"""
    #     search = SearchPage(drivers)
    #     search.input_search("selenium")
    #     search.click_search()
    #     result = re.search(r'selenium', search.get_source)
    #     log.info(result)
    #     assert result
    #
    # @allure.story("测试搜索候选用例")
    # def test_002(self, drivers):
    #     """测试搜索候选"""
    #     search = SearchPage(drivers)
    #     search.input_search("selenium")
    #     log.info(list(search.imagine))
    #     assert all(["selenium" in i for i in search.imagine])


if __name__ == '__main__':
    pytest.main(['TestCase/test_search.py', '--alluredir', './report/allure'])
    os.system('allure serve report/allure')
    #pytest.main(['TestCase/test_search.py'])