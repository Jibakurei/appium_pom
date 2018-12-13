from PO import gesture_mainpulation,creat_page,driver_configure
from Public import login_page,order_page
import unittest
import time
class test_appium(unittest.TestCase):
    @classmethod
    def setUp(cls):
        dconfigur = driver_configure.driver_configure()
        cls.driver = dconfigur.get_driver()
        cls.GM = gesture_mainpulation.gesture_mainpulation()
        cls.CreatPage = creat_page.CreatPage(cls.driver)
        cls.order_page = order_page.order_page(cls.driver)
        cls.login_page = login_page.login_page(cls.driver)

        
    def test_order(self):
        self.login_page.test_login("梁非凡","123123")
        self.order_page.test_order01("咖啡")
        self.GM.swipe_down(self.driver)
        self.order_page.test_order02()
        self.GM.swipe_downs(self.driver)
        time.sleep(5)

        try:
            shop_price = self.driver.find_element_by_id('com.yichuan:id/shop_price').get_attribute('name')
            price = print(shop_price.replace("￥","").replace("元",""))

        except Exception as e:
            print('shop_price定位失败')

        self.order_page.test_order03()

        try:
            goods_amount = self.driver.find_element_by_id('com.yichuan:id/tv_order_info_goods_amount').get_attribute('name')
            amount = print(goods_amount.replace("¥","").replace(" ",""))

        except Exception as e:
            print('goods_amount定位失败')

        self.assertEqual(price,amount,msg="商品总价对比不一致测试失败")

        self.order_page.test_quit()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()

            