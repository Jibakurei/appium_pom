from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Action(object):
    #初始化
    def __init__(self,se_driver):
        self.driver = se_driver

    def find_element(self,*loc):
        '''重写find_element方法，显式等待'''
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e
    def click(self,*loc):
        self.find_element(*loc).click()
    
    def clear(self,*loc):
        self.find_element(*loc).clear()
        
    def text(self,*loc):
        self.find_element(*loc).text

    def get_attribute(self,*loc):
        self.find_element(*loc).get_attribute("name")

    def send_keys(self,value,*loc):
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(value)
    


