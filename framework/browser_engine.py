import os.path
from configparser import  ConfigParser
from appium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):


    def appium_desired(self):
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path,encoding='utf-8')

        desired_caps={}
        desired_caps['platformName'] = config.get("phoneType","platformName")
        logger.info("You had select %s ." % desired_caps['platformName'])
        # 设备系统版本
        desired_caps['platformVersion'] = config.get("platformType","platformVersion")
        logger.info("You had select %s ." % desired_caps['platformVersion'])
        # 设备名称
        desired_caps['deviceName'] = config.get("deviceName","deviceName")
        logger.info("You had select %s ." % desired_caps['deviceName'])

        desired_caps['sessionOverride'] = config.get("sessionOverride","sessionOverride")

        dir = os.path.dirname(os.path.abspath('.'))
        desired_caps['app'] = dir+'/app/' + config.get("app","app")
        # desired_caps['app'] = file_path + config.get("app","app")

        logger.info("You had select %s ." % desired_caps['app'])


        desired_caps['noRest'] = config.get('noRest',"noRest")
        # 应用程序的包名
        desired_caps['appPackage'] = config.get("appPackage","appPackage")
        desired_caps['appActivity'] = config.get("appActivity","appActivity")

        logger.info("start run app......")

        desired_caps['ip'] = config.get('ip',"ip")
        desired_caps['port'] = config.get('port',"port")
        driver = webdriver.Remote('http://'+ str(desired_caps['ip'])+':'+str(desired_caps['port'])+'/wd/hub',desired_caps)
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        driver.implicitly_wait(5)
        logger.info("Set implicitly wait 5 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()

