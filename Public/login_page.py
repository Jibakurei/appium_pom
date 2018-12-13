# coding:utf-8
__author__ = 'Helen'
'''
description:登录页
'''
from PO import creat_page
from appium.webdriver.common import mobileby
import time

class login_page(creat_page.CreatPage):
    def test_login(self,username,passwrod):
        self.CreatPage = creat_page.CreatPage(self.driver)
        try:
            self.CreatPage.input_user(username)
        except Exception as e:
            print('user元素定位错误')

        try:
            self.CreatPage.input_Pws(passwrod)
        except Exception as e:
            print('Pws元素定位错误')

        try:
            self.CreatPage.click_btnLogin()
        except Exception as e:
            print('Login元素定位错误')
            time.sleep(5)


    def test_logins(self,username,passwrod):
        self.CreatPage = creat_page.CreatPage(self.driver)
        try:
            self.CreatPage.input_user(username)
        except Exception as e:
            print('user元素定位错误')

        try:
            self.CreatPage.input_Pws(passwrod)
        except Exception as e:
            print('Pws元素定位错误')

        try:
            self.CreatPage.click_btnLogin()
        except Exception as e:
            print('Login元素定位错误')
            time.sleep(5)


    def test_login_exit(self):
        self.CreatPage.click_me()
        self.CreatPage.click_mine()
        self.CreatPage.click_quit()
        self.CreatPage.click_btnNegative()
