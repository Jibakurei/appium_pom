import unittest
from PO import gesture_mainpulation,creat_page,driver_configure,start_motion_appium
from Public import login_page
from ddt import ddt,unpack,data
import csv


def get_data():
    value_rows = []
    with open(r'C:\\Users\\Administrator\\Desktop\\01.csv',encoding='gbk') as f:
        f_csv = csv.reader(f)
        next(f_csv)
        for r in f_csv:
            value_rows.append(r)
        return value_rows

@ddt
class test_appium(unittest.TestCase):
    start = start_motion_appium.start_motion_appium()
    try:
        start.start_motion()
    except Exception as e:
        print("模拟器启动失败")

    try:
        start.start_appium()
    except Exception as e:
        print("APPIUM启动失败")
    @classmethod
    def setUp(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()
        cls.GM = gesture_mainpulation.gesture_mainpulation()
        cls.login_page = login_page.login_page(cls.driver)
        cls.creat_page = creat_page.CreatPage(cls.driver)

    
    @data(*get_data())
    @unpack
    def test_06login(self,username,password):
        '''账户登录TEST'''
        self.login_page.test_logins(username, password)
        login = self.driver.find_element_by_id('com.yichuan:id/top_title').get_attribute('text')
        self.assertEquals("沂川登录",login,msg="文本对比不一致测试失败")
    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()