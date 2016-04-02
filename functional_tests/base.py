# coding:utf8
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys

class FunctionalTest(StaticLiveServerTestCase):
	"""docstring for FunctionalTest"""
	#@classmethod
	#def setUpClass(cls):
	#	cls.browser = webdriver.Firefox()

	#@classmethod
	#def tearDownClass(cls):
	#	cls.browser.close()

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(2)

	def tearDown(self):
		self.browser.refresh()
		self.browser.quit()

	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])
		
	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_text')
