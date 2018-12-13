from PO import creat_page
from appium.webdriver.common import mobileby
import time
import unittest
class order_page(creat_page.CreatPage):
    def test_order01(self,content):
        '''商品搜索选择'''
        try:
            self.CreatPage = creat_page.CreatPage(self.driver)
            self.CreatPage.click_open()
            self.CreatPage.click_submit()
            self.CreatPage.click_search_content()
            self.CreatPage.input_content(content)
            self.CreatPage.click_search()
            self.CreatPage.click_title()
            self.CreatPage.click_buy()
            self.CreatPage.click_right()
            time.sleep(5)
        except Exception as e:
            print("商品选择元素定位失败")

    def test_order02(self):
        '''商品结算'''
        try:
            self.CreatPage = creat_page.CreatPage(self.driver)
            time.sleep(5)
            self.CreatPage.click_finish()
            time.sleep(5)
            self.CreatPage.click_buy()
            self.CreatPage.click_balance()
            self.CreatPage.clear_et_num()
            self.driver.press_keycode(8)
            self.driver.press_keycode(9)
            self.driver.press_keycode(10)
            self.driver.press_keycode(8)
            self.driver.press_keycode(9)
            self.driver.press_keycode(10)
            self.CreatPage.click_bt_get()
        except Exception as e:
            print("下单结算元素定位失败")
            
            shop_price = self.CreatPage.text_shop_price()
    def test_order03(self):
        '''订单详情'''
        try:
            self.CreatPage.click_tv_post()
            self.driver.press_keycode(4)
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)
            self.driver.press_keycode(4)
            time.sleep(2)
            self.driver.press_keycode(4)
            self.CreatPage.click_me()
            self.CreatPage.click_send_loc()
            self.CreatPage.click_goods_count()
            time.sleep(2)
        except Exception as e:
            print("提交订单后元素定位失败")

    def test_quit(self):
        '''退出操作'''
        self.driver.press_keycode(4)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.CreatPage.click_mine()
        self.CreatPage.click_quit()
        self.CreatPage.click_btnNegative()


