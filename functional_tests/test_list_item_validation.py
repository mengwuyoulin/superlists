# coding:utf8
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	"""docstring for ItemValidationTest"""
	def test_cannot_add_empty_list_items(self):
		#小明不小心提交了一个空待办事项
		#输入框中没输入内容，他就按下了回车键
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		#首页刷新了，显示一个错误消息
		#提示待办事项不能为空
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text,'提示待办事项不能为空')

		#他输入一些文字，然后再次提交，这次没问题了
		self.browser.find_element_by_id('id_new_item').send_keys('买花生\n')
		self.check_for_row_in_list_table('1:买花生')

		#他有点调皮，又提交了一个空待办事项
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		#在清单页面中他看到了一个类似的错误消息
		self.check_for_row_in_list_table('1:买花生')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text,'提示待办事项不能为空')

		#输入文字之后就没问题了
		self.browser.find_element_by_id('id_new_item').send_keys('散步\n')
		self.check_for_row_in_list_table('1:买花生')
		self.check_for_row_in_list_table('2:散步')
		#self.fail('write me!')		
