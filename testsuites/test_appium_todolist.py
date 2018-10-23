from pageobjects.homepage import Homepage
from testsuites.base_testcase import BaseTestCase
import time
from pageobjects.addpage import Addpage
from pageobjects.deletepage import Deletepage



class TodolistSearch(BaseTestCase):
    def test_login_action(self):
        home_page = Homepage(self.driver)
        home_page.Login('1','1')

        add_page = Addpage(self.driver)
        add_page.Login('sdagkjfgslgjfkgjdfkgjkdfjg')
        time.sleep(3)

        delete_page = Deletepage(self.driver)
        delete_page.Login()

