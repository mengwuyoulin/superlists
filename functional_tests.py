# coding:utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
	"""docstring for NewVisitorTest"""
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(2)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		#小明听说有一个很酷的在线待办事项应用
		#他去看了这个应用的首页

		self.browser.get("http://localhost:8000")

		#他注意到网页的标题和头部都包含“To-Do”这个词

		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		#应用邀请他输入一个待办事项
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		#他在一个文本框中输入了“购买乒乓球”
		#小明是一个乒乓球爱好者
		inputbox.send_keys('Buy PingPang')

		#他按回车键后，页面更新了
		#待办事项表格中显示了“1：购买乒乓球”
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1:Buy PingPang')
	
		#代码异味，要重写的部分
		#table = self.browser.find_element_by_id('id_list_table')		
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertTrue(
		#	any(row.text == '1:Buy PingPang' for row in rows),
		#	"New to-do item did not appear in table -- its text was:\n%s"%(table.text,)
		#)
		#self.assertIn('1:Buy PingPang',[row.text for row in rows])
		
		#页面中又显示了一个文本框，可以输入其他的待办事项
		#他输入了“约上小何去打乒乓球”
		#小明做事很有计划
		inputbox=self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys("Meet xiaohe to play PingPang")
		inputbox.send_keys(Keys.ENTER)
		
		#页面再次刷新，他的清单中显示了这两个待办事项
		self.check_for_row_in_list_table('1:Buy PingPang')
		self.check_for_row_in_list_table('6:Meet xiaohe to play PingPang')
		
		#小明想知道这个网站是否会记住他的清单
		time.sleep(3)
		#他看到网站为他生成了一个唯一的URL
		#而且页面中有一些文字解说这个功能
		self.fail('Finiesh the test!')

		#他访问那个URL，发现他的待办事项列表还在

		#他很满意，就去睡觉了


if __name__ == '__main__':
	unittest.main(warnings='ignore')
		
