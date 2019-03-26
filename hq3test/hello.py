# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2019/03/26 QTAF自动生成

from hq3lib.testcase import Hq3TestCase

class HelloTest(Hq3TestCase):
    '''示例测试用例
    '''
    owner = "root"
    timeout = 5
    priority = Hq3TestCase.EnumPriority.High
    status = Hq3TestCase.EnumStatus.Design
    
    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)
    
if __name__ == '__main__':
    HelloTest().debug_run()

