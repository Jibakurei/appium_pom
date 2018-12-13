# coding:utf-8
__author__ = 'Helen'
'''
description:测试登录和退出功能
'''
import unittest
import time
from PO import gesture_mainpulation,creat_page,driver_configure
from Public import login_page

class test_appium(unittest.TestCase):
    @classmethod
    def setUp(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()
        cls.GM = gesture_mainpulation.gesture_mainpulation()
        cls.login_page = login_page.login_page(cls.driver)
        cls.creat_page = creat_page.CreatPage(cls.driver)


    def test_01login(self):
        '''正确账户密码'''
        self.login_page.test_login("梁非凡","123123")
        text = self.driver.find_element_by_id('com.yichuan:id/tv_search_content').text
        self.assertEqual('999,999,999件商品任你选',text,msg="文本对比不一致测试失败")
        self.login_page.test_login_exit()
    
    def test_02login(self):
        '''错误账户密码'''
        self.login_page.test_logins("lowisn","123123")
        time.sleep(2)
        login = self.driver.find_element_by_id('com.yichuan:id/top_title').get_attribute('text')
        self.assertEquals("沂川登录",login,msg="文本对比不一致测试失败")

    def test_03login(self):
        '''正确账户错误密码'''
        self.login_page.test_logins("梁非凡","1231231")
        login = self.driver.find_element_by_id('com.yichuan:id/top_title').get_attribute('text')
        self.assertEquals("沂川登录",login,msg="文本对比不一致测试失败")

    def test_04login(self):
        '''空账户密码'''
        self.login_page.test_logins("","123123")
        login = self.driver.find_element_by_id('com.yichuan:id/top_title').get_attribute('text')
        self.assertEquals("沂川登录",login,msg="文本对比不一致测试失败")

    def test_05login(self):
        '''小于六个字符账户密码'''
        self.login_page.test_logins("low","123")
        login = self.driver.find_element_by_id('com.yichuan:id/top_title').get_attribute('text')
        self.assertEquals("沂川登录",login,msg="文本对比不一致测试失败")

    def test_06login(self):
        '''正确账户空密码'''
        self.login_page.test_logins("lowisn","")
        login = self.driver.find_element_by_id('com.yichuan:id/top_title').get_attribute('text')
        self.assertEquals("沂川登录",login,msg="文本对比不一致测试失败")
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()