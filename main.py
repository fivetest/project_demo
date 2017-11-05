#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: samren
import time
import unittest
import HTMLTestRunner
from testcases.bugfree_admin_login_logout_chrome import BugfreeAdminLoginLogout 


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(BugfreeAdminLoginLogout))

    fp = file('./reports/test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"Bugfree项目的测试报告",
        description=u"详细信息如下"
    )
    runner.run(suite)
    fp.close()