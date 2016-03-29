from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item
# Create your tests here.
class ItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		#创建一个对象
		first_item = Item()
		#给属性赋值
		first_item.text = 'The first (ever) list item'
		#调用.save()
		first_item.save()

		second_item = Item()
		second_item.text = 'Ietem the second'
		second_item.save()

		#.objects查询数据库的AIP，类属性；.all 查询方法 返回所有的记录，结果：类似列表的对象QuerySet
		saved_items = Item.objects.all()
		#检查存储在数据库中的对象，看保存的信息是否正确
		self.assertEqual(saved_items.count(),2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text,'The first (ever) list item')
		self.assertEqual(second_saved_item.text,'Ietem the second')

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(),expected_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home_page(request)

		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text,'A new list item')

	def test_home_page_redirects_after_POST(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home_page(request)

		self.assertEqual(response.status_code,302)
		self.assertEqual(response['location'],'/')
		
	def test_home_page_only_saves_items_when_necessary(self):
		request = HttpRequest()
		home_page(request)
		self.assertEqual(Item.objects.count(),0)

	def test_home_page_displays_all_list_items(self):
		Item.objects.create(text='itemey 1')
		Item.objects.create(text='itemey 2')

		request = HttpRequest()
		response = home_page(request)

		self.assertIn('itemey 1',response.content.decode())
		self.assertIn('itemey 2',response.content.decode())