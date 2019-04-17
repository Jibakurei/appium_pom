import unittest
from PO import gesture_mainpulation,creat_page,driver_configure
from Public import login_page
from ddt import ddt,unpack,data
import csv
# TestCase = csv.reader(open('C:\\Users\\Administrator\\Desktop\\01.csv','r'))

# users = []
# for i in TestCase:
#     user = []
#     for j in i:
#         user.append(j)
#         users.append(user)


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
    @classmethod
    def setUp(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()
        cls.GM = gesture_mainpulation.gesture_mainpulation()
        cls.login_page = login_page.login_page(cls.driver)
        cls.creat_page = creat_page.CreatPage(cls.driver)
    
    
    
    # def login(self):
    #     i = 0
    #     for user in users:
    #         print(user[0])
    #         if user[0] == 'null':
    #             username = user[i][1]
    #             password = user[i][2]
    #             break; 
    #         else:
    #             i+=1
    #         self.login_page.test_login(username,password)
    
    # def login1(self):
    #     username = user[1][1]
    #     passwrod = user[1][2]
    #     self.login_page.test_login(username,passwrod)
    @data(*get_data())
    @unpack
    def test_06login(self,username,password):
        '''正确账户空密码'''
        self.login_page.test_logins(username, password)
        login = self.driver.find_element_by_id('com.yichuan:id/top_title').get_attribute('text')
        self.assertEquals("沂川登录",login,msg="文本对比不一致测试失败")
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()