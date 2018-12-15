"""
    目标：PO模式scripts脚本实现
    操作：
        1. 新建测试模块(test_页面对象.py)
        2. 类名(使用大驼峰去掉下划线)
        3. 不用过脑(def setup_class teardown_class test_login)编写三个方法
            setup_class
                1. 实例化 page页面对象
            teardown_class
                1. 关闭 driver对象
            test_login()
                1.根据操作步骤调用page对象内方法
                2. 断言
                3. 截图
"""
import sys
import os
sys.path.append(os.getcwd())

import pytest
from base.get_driver import get_driver
from page.page_login import PageLogin


# 建类名


class TestLogoin():
    # setup_class
    def setup_class(self):
        # 实例化 page页面对象
        self.login = PageLogin(get_driver())

    # teardown_class
    def teardown_class(self):
        # 关闭驱动对象
        self.login.driver.quit()

    # test_login
    @pytest.mark.parametrize("username,password",[("18611110000","123456")])
    def test_login(self,username,password):
        # 输入用户名
        self.login.page_input_username(username)
        # 输入密码
        self.login.page_input_password(password)
        # 点击登录
        self.login.page_click_login_btn()