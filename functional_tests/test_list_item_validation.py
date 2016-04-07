# coding:utf8
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	"""docstring for ItemValidationTest"""
	def test_cannot_add_duplicate_items(self):
		#小明访问首页，新建了一个清单
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('慢跑健身\n')
		self.check_for_row_in_list_table('1:慢跑健身')

		#他不小心输入了一个重复的待办事项
		self.get_item_input_box().send_keys('慢跑健身\n')

		#他看到有一条帮助的错误消息
		self.check_for_row_in_list_table('1:慢跑健身')
		error = self.get_error_element()
		self.assertEqual(error.text,"你已经添加过此事项！")

	def test_cannot_add_empty_list_items(self):
		#小明不小心提交了一个空待办事项
		#输入框中没输入内容，他就按下了回车键
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')

		#首页刷新了，显示一个错误消息
		#提示待办事项不能为空
		error = self.get_error_element()
		self.assertEqual(error.text,'待办事项不能为空')

		#他输入一些文字，然后再次提交，这次没问题了
		self.get_item_input_box().send_keys('买花生\n')
		self.check_for_row_in_list_table('1:买花生')

		#他有点调皮，又提交了一个空待办事项
		self.get_item_input_box().send_keys('\n')

		#在清单页面中他看到了一个类似的错误消息
		self.check_for_row_in_list_table('1:买花生')
		error = self.get_error_element()
		self.assertEqual(error.text,'待办事项不能为空')

		#输入文字之后就没问题了
		self.get_item_input_box().send_keys('散步\n')
		self.check_for_row_in_list_table('1:买花生')
		self.check_for_row_in_list_table('2:散步')
		#self.fail('write me!')		

	def test_error_messages_are_cleared_on_input(self):
		#小明新建了一个清单，但方法不当，所以出现了一个验证错误
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')
		error = self.get_error_element()
		self.assertTrue(error.is_displayed())

		#为了消除错误，他开始在输入框中输入内容
		self.get_item_input_box().send_keys('遛狗')

		#他看到错误消失了，很高兴
		error = self.get_error_element()
		self.assertFalse(error.is_displayed())

	def get_error_element(self):
		return self.browser.find_element_by_css_selector('.has-error')