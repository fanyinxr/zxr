import unittest
from framework.browser_engine import BrowserEngine
import os
import time

apk_path = os.path.dirname(os.path.abspath('.'))
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine()
        self.driver = browser.appium_desired()


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
