from appium.webdriver.common.mobileby import By
from pageobjects.base import BasePage


class Addpage(BasePage):
    #新建待办事项
    home_page_addname_search_loc = (By.ID, 'com.example.todolist:id/action_new')
    home_page_addtext_search_loc = (By.ID, 'com.example.todolist:id/toDoItemDetailET')
    home_page_addbtn_search_loc = (By.ID, 'com.example.todolist:id/saveBtn')

    def Login(self,text):
        self.click(*self.home_page_addname_search_loc)
        self.sendkeys(text,*self.home_page_addtext_search_loc)
        self.click(*self.home_page_addbtn_search_loc)