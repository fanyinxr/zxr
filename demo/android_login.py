import os
from appium import webdriver
import unittest
import time
from appium.webdriver.common.touch_action import TouchAction

apk_path = os.path.dirname(os.path.abspath('.'))
class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        # 设备系统版本
        desired_caps['platformVersion'] = '6.0'
        # desired_caps['platformVersion'] = '7.1.2'
        # 设备名称
        desired_caps['deviceName'] = '127.0.0.1:21503'
        # desired_caps['deviceName'] = '8eaafc7a'
        desired_caps['sessionOverride'] = True
        desired_caps['app'] = apk_path + '/app/todolist.apk'
        desired_caps['noRest'] = True
        # 应用程序的包名
        desired_caps['appPackage'] = 'com.example.todolist'
        desired_caps['appActivity'] = 'com.example.todolist.LoginActivity'

        # 启动app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_login_contacts(self):
        #用户登录
        self.driver.find_element_by_id('com.example.todolist:id/nameET').send_keys('1')
        self.driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys('1')
        # self.driver.find_element_by_id('com.example.todolist:id/loginBtn').click()
        self.driver.find_element_by_xpath('//android.widget.Button').click()
        time.sleep(5)

        #添加待办事项
        # self.driver.find_element_by_id('com.example.todolist:id/action_new').click()
        self.driver.find_element_by_accessibility_id("新建待办事项").click()
        self.driver.find_element_by_id('com.example.todolist:id/toDoItemDetailET').send_keys('aabbcchhh')
        self.driver.find_element_by_id('com.example.todolist:id/saveBtn').click()

        #删除
        el=self.driver.find_element_by_id('com.example.todolist:id/toDoItemDetailTv')
        TouchAction(self.driver).long_press(el,duration=1000).perform()

        self.driver.find_element_by_xpath('//android.widget.TextView[@text="删除"]').click()
        self.driver.find_element_by_id('android:id/button1').click()
