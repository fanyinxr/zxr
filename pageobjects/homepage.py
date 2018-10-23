from appium.webdriver.common.mobileby import By
from pageobjects.base import BasePage


class Homepage(BasePage):
    #用户登录
    home_page_loginname_search_loc = (By.ID, 'com.example.todolist:id/nameET')
    home_page_loginpwd_search_loc = (By.ID, 'com.example.todolist:id/passwordET')
    home_page_loginbtn_search_loc = (By.XPATH, '//android.widget.Button')

    def Login(self,name,pwd):
        self.sendkeys(name,*self.home_page_loginname_search_loc)
        self.sendkeys(pwd,*self.home_page_loginpwd_search_loc)
        self.click(*self.home_page_loginbtn_search_loc)