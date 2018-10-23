from framework.logger import Logger
import time
import os.path
from appium.webdriver.common.touch_action import TouchAction

logger = Logger(logger="BasePage").getlog()

class BasePage(object):
    """
    主要是把常用的几个selenium方法封装到BasePage这几个类
    """
    def __init__(self,driver):
        self.driver = driver

    def back(self):
        #后退按钮
        self.driver.back()
        logger.info("返回键")

    def forward(self):
        #前进按钮
        self.driver.forward()
        logger.info("Click forward on current page.")


    def open_url(self,url):
        #打开URL站点
        self.driver.get(url)

    def quit_browser(self):
        #关闭并停止浏览器服务
        self.driver.quit()

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except Exception as e:
            logger.error("Failed to quit the browser with %s" %e)

    def find_element(self,*loc):
        try:
            return self.driver.find_element(*loc)
            logger.info("找到页面元素-->",loc)
        except:
            #print("%s 页面中未能找到 %s 元素" %(self,loc))
            logger.error("%s 页面中未能找到 %s 元素" %(self,loc))

            #保存图片
    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots'
        rq = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to floder : /screenshots")
        except Exception as e:
            print("截图错误！！！")
            logger.error("Failed to take screenshot! %s" % e)

    #输入
    def sendkeys(self,text,*loc):
        el = self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("The element %s was send." % el.text)

        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to sendkeys the element with %s" % e)

    #清除文本框
    def clear(self,*loc):
        el = self.find_element(*loc)
        try:
            el.clear()
        except Exception as e:
            self.get_windows_img()

    #点击元素
    def click(self,*loc):
        el = self.find_element(*loc)
        try:

            print("The element %s was clicked" % el.text)
            el.click()
            #引入模块找不见报NameError的错
        except NameError as e:
            print("Failed to click the element with %s" % e)

    #跳转窗口
    def window(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])  # 页面切换


    #frame
    def frame(self):
        self.driver.switch_to.frame("main")

    def text(self,*loc):
        el = self.find_element(*loc)
        print(el.text)


    #长按
    def TouchAction(self,*loc):
        el = self.find_element(*loc)
        TouchAction(self.driver).long_press(el,duration=1000).perform()








