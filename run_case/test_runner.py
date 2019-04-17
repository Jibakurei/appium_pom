import unittest
import sys
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
import time
import HTMLTestReportCN
import HTMLTestRunner
# from TestCase.Test_login import test_appium
from TestCase.Test_csv_login import test_appium
# from TestCase.Test_order_process import test_appium




if __name__ == '__main__':

    #testunit = unittest.TestSuite()
    #testunit.addTest(logins('test_login1'))

    #根目录
    project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
    #用例目录
    test_case_path = project_path+"\\Testcase"

    # suite = unittest.defaultTestLoader.discover(start_dir=test_case_path,pattern='test*.py')

    suite = unittest.TestSuite(unittest.makeSuite(test_appium))  

    # 定义报告输出路径

    report_path = project_path+"\\Result\\"
    
    report_name = report_path+time.strftime('%Y%m%d%H%M%S', time.localtime())


    # report_path =os.path.dirname(os.path.abspath('.'))+'/Result/'

    # now = time.strftime('%Y-%m-%D-%h_%m_%S',time.localtime(time.time()))

    HTMLfile = report_name + "_Report.html"
    
    fp = open(HTMLfile, "wb")

    

    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, 
           title=u"沂川商城回归测试", 
           description=u"测试用例结果")

    runner.run(suite)

    fp.close()