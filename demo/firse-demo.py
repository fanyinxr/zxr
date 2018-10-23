import os
from appium import webdriver

# #自动化安装apk包到手机

apk_path = os.path.dirname(os.path.abspath('.'))
desired_caps={}
#设备系统
desired_caps['platformName']='Android'
#设备系统版本
desired_caps['platformVersion']='6.0'
#设备名称
desired_caps['deviceName']='127.0.0.1:21503'

desired_caps['sessionOverride']=True

#测试apk包的路径
desired_caps['app']=apk_path+'/app/todolist.apk'
#不需要每次都安装apk
desired_caps['noRest']=True
#应用程序的包名
desired_caps['appPackage']='com.example.todolist'
desired_caps['appActivity']='com.example.todolist.LoginActivity'

#启动app
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.find_element_by_id('com.example.todolist:id/nameET').send_keys('1')
driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys('1')
driver.find_element_by_id('com.example.todolist:id/loginBtn').click()
