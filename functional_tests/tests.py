# coding:utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
	"""docstring for NewVisitorTest"""
	def setUp(self):
		self.browser = webdriver.Ie()
		self.browser.implicitly_wait(2)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])


	def test_layout_and_styling(self):
		#小明访问首页
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)

		#他看到输入框完美地居中显示
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta =20
		)

		#他新建了一个清单，看到输入框仍完美地居中显示
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta =20
		)

	def test_can_start_a_list_and_retrieve_it_later(self):
		#小明听说有一个很酷的在线待办事项应用
		#他去看了这个应用的首页

		self.browser.get(self.live_server_url)

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
		inputbox.send_keys('买乒乓球')

		#他按回车键后，他被带到了一个新URL
		#待办事项表格中显示了“1：购买乒乓球”
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url,'/lists/.+')
		self.check_for_row_in_list_table('1:买乒乓球')
	
		#页面中又显示了一个文本框，可以输入其他的待办事项
		#他输入了“约上小何去打乒乓球”
		#小明做事很有计划
		inputbox=self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys("约上朋友打乒乓球")
		inputbox.send_keys(Keys.ENTER)
		
		#页面再次刷新，他的清单中显示了这两个待办事项
		self.check_for_row_in_list_table('1:买乒乓球')
		self.check_for_row_in_list_table('2:约上朋友打乒乓球')
		
		#现在一个叫小路的新用户访问了网站

		##我们使用一个新浏览器会话
		self.browser.quit()
		##确保小明的信息不回从cookie中泄露出来#
		self.browser = webdriver.Ie()

		#小路访问首页
		#页面看不到小明的清单
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('约上朋友打乒乓球',page_text)
		self.assertNotIn('买乒乓球',page_text)

		#小路输入一个新待办事项，新建一个清单
		#他不像小明那么兴趣盎然
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('买牛奶')
		inputbox.send_keys(Keys.ENTER)

		#小路看到网站为他生成了一个唯一的URL
		xiaolu_list_url = self.browser.current_url
		self.assertRegex(xiaolu_list_url,'/lists/.+')
		self.assertNotEqual(xiaolu_list_url,edith_list_url)

		#这个页面还是没有小明的清单
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('约上朋友打乒乓球',page_text)
		self.assertIn('买牛奶',page_text)
		#而且页面中有一些文字解说这个功能
	

		#他访问那个URL，发现他的待办事项列表还在

		#他很满意，就去睡觉了



		
