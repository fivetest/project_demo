# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time
from lib.utils import captureScreen
import ddt

L = [['admin', '123456', u'退出']]


@ddt.ddt
class BugfreeAdminLoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"

    @ddt.unpack
    @ddt.data(*L)
    def test_login(self, username, password, flag):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys(username)
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys(password)
        driver.find_element_by_id("LoginForm_rememberMe").click()
        driver.find_element_by_id("SubmitLoginBTN").click()
        captureScreen(driver)
        time.sleep(3)
        self.assertIn(flag, driver.page_source)
    
    # def test_bugfree_admin_login_logout(self):
    #     driver = self.driver
    #     driver.find_element_by_link_text(u" 新建 Bug   ").click()
    #     time.sleep(2)
    #     # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | 新建Bug | ]]
    #     driver.switch_to.window(driver.window_handles[1])
    #     driver.find_element_by_id("BugInfoView_title").clear()
    #     driver.find_element_by_id("BugInfoView_title").send_keys("autotest002")
    #     driver.find_element_by_id("BugInfoView_assign_to_name").click()
    #     driver.find_element_by_css_selector("li.ac_even").click()
    #     driver.find_element_by_id("BugInfoView_mail_to").click()
    #     driver.find_element_by_xpath("//div[5]/ul/li").click()
    #     Select(driver.find_element_by_id("BugInfoView_severity")).select_by_visible_text("1")
    #     Select(driver.find_element_by_id("Custom_BugType")).select_by_visible_text(u"代码错误")
    #     Select(driver.find_element_by_id("Custom_HowFound")).select_by_visible_text(u"单元测试")
    #     driver.find_element_by_id("Custom_OpenedBuild").clear()
    #     driver.find_element_by_id("Custom_OpenedBuild").send_keys("001")
    #     driver.find_element_by_name("yt0").click()
    #     time.sleep(3)

    # def test_nothing(self):
    #     print "nothing to do"

    def tearDown(self):
        #self.driver.find_element_by_link_text(u"退出").click()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
