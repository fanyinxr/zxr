from appium.webdriver.common.mobileby import By
from pageobjects.base import BasePage
from appium.webdriver.common.touch_action import TouchAction


class Deletepage(BasePage):
    # 新建待办事项
    home_page_text_search_loc = (By.ID, 'com.example.todolist:id/toDoItemDetailTv')
    home_page_deletename_search_loc = (By.XPATH,'//android.widget.TextView[@text="删除"]')
    home_page_deleteDetermine_search_loc = (By.ID,'android:id/button1')

    def Login(self):

        self.TouchAction(*self.home_page_text_search_loc)
        self.click(*self.home_page_deletename_search_loc)
        self.click(*self.home_page_deleteDetermine_search_loc)
