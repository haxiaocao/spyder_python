# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 00:02:20 2017

@author: QingqingXiaocao
"""

#Selenium 是什么？一句话，自动化测试工具。它支持各种浏览器，可以安装位浏览器插件，而且
#它本身就是浏览器；

# phnantomjs的效率高（没有界面的浏览器）
#Python＋Selenium＋PhantomJS 的无缝对接了嘛！PhantomJS 用来渲染解析JS，
#Selenium 用来驱动以及与 Python 的对接，Python 进行后期的处理，完美的三剑客！
#Selenium 2，又名 WebDriver

#reference: http://www.51testing.com/zhuanti/webdriver.htm
#http://cuiqingcai.com/2599.html
#http://www.seleniumhq.org/docs/index.jsp
#http://selenium-python.readthedocs.io/index.html


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#==============================================================================
#brower=webdriver.Chrome()
#brower.get('http://www.python.org')
# assert "python" in brower.title   # this will cause exception 
# elem=brower.find_element_by_name('q')
# elem.send_keys('pycon')
# elem.send_keys(Keys.RETURN)
# print brower.page_source
#==============================================================================

#==============================测试用例============================================
# #获取网页渲染后的源代码。
# #输出 page_source 属性即可。
# class PythonOrgSearch(unittest.TestCase):
#  
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#  
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
#  
#     def tearDown(self):
#         self.driver.close()
#  
# if __name__ == "__main__":
#     unittest.main()
# 
# #The test case class is inherited from unittest.TestCase. 
# #Inheriting from TestCase class is the way to tell unittest module 
# #that this is a test case. The setUp is part of initialization,
# # this method will get called before every test function which you are 
# # going to write in this test case class. The test case method should always 
# # start with characters test. The tearDown method will get called after 
# # every test method. This is a place to do all cleanup actions.
# # You can also call quit method instead of close. 
# # The quit will exit the entire browser, whereas close will close a tab, 
# # but if it is the only tab opened, by default most browser will exit entirely.
#==============================================================================


#==============================模拟输入=======================================
# driver=webdriver.Chrome()
# element = driver.find_element_by_id("passwd-id")
# element = driver.find_element_by_name("passwd")
# element = driver.find_elements_by_tag_name("input")
# element = driver.find_element_by_xpath("//input[@id='passwd-id']")
# 
# element = driver.find_element_by_id("passwd-id")
# element = driver.find_element_by_name("passwd")
# element = driver.find_elements_by_tag_name("input")
# element = driver.find_element_by_xpath("//input[@id='passwd-id']")
# element.send_keys("some text")  #input textbox
# element.send_keys("and some",Keys.ARROW_DOWN)  #模拟点击按键
# element.clear()
# 
#==============================================================================
#=============================填充表单============================================
# 
# driver=webdriver.Chrome()
# element = driver.find_element_by_xpath("//select[@name='name']")
# all_options = element.find_elements_by_tag_name("option")
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()
# 
# #选择表单。
# from selenium.webdriver.support.ui import Select
# select = Select(driver.find_element_by_name('name'))
# select.select_by_index(index)
# select.select_by_visible_text("text")
# select.select_by_value(value)
# 
# select = Select(driver.find_element_by_id('id'))
# select.deselect_all()
# 
# driver.find_element_by_id("submit").click()  # 提交表单
#==============================================================================
#============================元素拖拽==============================================
# element = driver.find_element_by_name("source")
# target = driver.find_element_by_name("target")
# 
# from selenium.webdriver import ActionChains
# action_chains = ActionChains(driver)
# action_chains.drag_and_drop(element, target).perform()
# 
#==============================================================================
#============================cookie处理===============================================
# 
# # Go to the correct domain
# driver.get("http://www.example.com")
# 
# # Now set the cookie. This one's valid for the entire domain
# cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
# driver.add_cookie(cookie)
#==============================================================================


#===========================显示等待============================================
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# 
# driver = webdriver.Chrome()
# driver.get("http://somedomain/url_that_delays_loading")
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# finally:
#     driver.quit()
#==============================================================================
#================================隐式等待==========================================
# 
# from selenium import webdriver
# 
# driver = webdriver.Chrome()
# driver.implicitly_wait(10) # seconds
# driver.get("http://somedomain/url_that_delays_loading")
# myDynamicElement = driver.find_element_by_id("myDynamicElement")
#==============================================================================



