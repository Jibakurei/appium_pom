import time

from appium.webdriver.common import mobileby

from PO.Base_Page import Action


class CreatPage(Action):
    
    by = mobileby.MobileBy()
    btnClick_loc =(by.ID,"com.yichuan:id/tv_start")
    etUser_loc = (by.ID,"com.yichuan:id/et_username")
    etPws_loc = (by.ID,"com.yichuan:id/et_password")
    btnLogin_loc = (by.ID,"com.yichuan:id/login_tv_login")
    me_loc = (by.ID,"com.yichuan:id/tab_button_mine")
    mine_loc = (by.ID,"com.yichuan:id/mine_ll_center")
    quit_loc = (by.ID,"com.yichuan:id/mine_btn_exit")
    btnNegative_loc = (by.ID,"com.yichuan:id/btnNegative")
    open_loc = (by.ID,"com.yichuan:id/iv_open_close")
    close_loc = (by.ID,"com.yichuan:id/iv_open_close")
    submit_loc = (by.ID,"com.yichuan:id/btn_submit_location")
    search_content_loc = (by.ID,"com.yichuan:id/tv_search_content")
    et_keywords_loc = (by.ID,"com.yichuan:id/et_keywords")
    search_loc = (by.ID,"com.yichuan:id/tv_search")
    goods_title_loc = (by.ID,"com.yichuan:id/tv_goods_title")
    goods_buy_loc = (by.ID,"com.yichuan:id/tv_buy_at_once")
    changenum_right_loc = (by.ID,"com.yichuan:id/changenum_right")
    finish_loc = (by.ID,"com.yichuan:id/tv_finish")
    balance_loc = (by.ID,"com.yichuan:id/order_ll_balance")
    et_num_loc = (by.ID,"com.yichuan:id/coupons_et_num")
    bt_get_loc = (by.ID,"com.yichuan:id/coupons_bt_get")
    tv_post_loc = (by.ID,"com.yichuan:id/order_tv_post")
    send_loc = (by.ID,"com.yichuan:id/mine_ll_send")
    shop_price_loc = (by.ID,"com.yichuan:id/order_tv_price")
    goods_amount_loc = (by.ID,"com.yichuan:id/tv_order_info_goods_amount")
    goods_count_loc = (by.ID,"com.yichuan:id/tv_goods_count")
    top_title_loc = (by.ID,"com.yichuan:id/top_title")


    def text_top_title(self):
        '''顶部文字'''
        self.text(*self.top_title_loc)

    def click_goods_count(self):
        '''订单详情'''
        self.click(*self.goods_count_loc)

    def click_send_loc(self):
        '''待发货订单'''
        self.click(*self.send_loc)

    def text_goods_amount(self):
        '''商品总价'''
        self.get_attribute(*self.goods_amount_loc)

    def text_shop_price(self):
        '''商品价格'''
        self.get_attribute(*self.shop_price_loc)
        
    def click_balance(self):
        '''余额'''
        self.click(*self.balance_loc)
        
    def clear_et_num(self):
        '''余额输入框清除'''
        self.clear(*self.et_num_loc)
        
    def input_et_num(self,num):
        '''余额输入框'''
        self.send_keys(num,*self.et_num_loc)
        
    def click_et_num(self):
        '''点击余额输入框'''
        self.click(*self.et_num_loc)

    def click_bt_get(self):
        '''余额确认'''
        self.click(*self.bt_get_loc)

    def click_tv_post(self):
        '''提交订单'''
        self.driver.tap([(564,1088),(768,1184)],50)
        # self.click(*self.tv_post_loc)

    def click_open(self):
        '''展开'''
        self.click(*self.open_loc)

    def click_close(self):
        '''缩放'''
        self.click(*self.close_loc)

    def click_submit(self):
        '''提交'''
        self.click(*self.submit_loc)

    def click_search_content(self):
        '''搜索框'''
        self.click(*self.search_content_loc)
        
    def click_search(self):
        '''搜索'''
        self.click(*self.search_loc)

    def click_title(self):
        '''商品标题'''
        self.click(*self.goods_title_loc)

    def click_buy(self):
        '''购买'''
        self.click(*self.goods_buy_loc)

    def click_right(self):
        '''数量选择'''
        self.click(*self.changenum_right_loc)

    def click_finish(self):
        '''完成'''
        self.click(*self.finish_loc)

    def input_content(self,content):
        '''搜索内容'''
        self.send_keys(content,*self.et_keywords_loc)

    def click_mine(self):
        '''个人中心'''
        self.click(*self.mine_loc)

    def click_quit(self):
        '''退出'''
        self.click(*self.quit_loc)

    def click_btnNegative(self):
        '''确认退出'''
        self.click(*self.btnNegative_loc)

    def click_me(self):
        '''我的'''
        self.click(*self.me_loc)

    def input_user(self,username):
        '''用户'''
        self.send_keys(username,*self.etUser_loc)

    def user_clear(self):
        '''用户清除'''
        self.clear(*self.etUser_loc)

    def input_Pws(self,password):
        '''密码'''
        self.send_keys(password,*self.etPws_loc)

    def pws_clear(self):
        '''密码清除'''
        self.clear(*self.etPws_loc)

    def click_btnLogin(self):
        '''登录'''
        self.click(*self.btnLogin_loc)
