# coding:utf8
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
	"""docstring for NewVisitorTest"""

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

