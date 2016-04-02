from django.test import TestCase
from django.core.exceptions import ValidationError

from lists.models import Item,List

# Create your tests here.
class ListAndItemModelTest(TestCase):

	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_		
		first_item.save()

		second_item = Item()
		second_item.text = 'Ietem the second'
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list,list_)

		#.objects查询数据库的AIP，类属性；.all 查询方法 返回所有的记录，结果：类似列表的对象QuerySet
		saved_items = Item.objects.all()
		#检查存储在数据库中的对象，看保存的信息是否正确
		self.assertEqual(saved_items.count(),2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text,'The first (ever) list item')
		self.assertEqual(first_saved_item.list,list_)
		self.assertEqual(second_saved_item.text,'Ietem the second')
		self.assertEqual(second_saved_item.list,list_)
	def test_cannot_save_empty_list_items(self):
		list_ = List.objects.create()
		item = Item(list = list_,text = '')
		with self.assertRaises(ValidationError):
			item.save()
			item.full_clean()

	def test_get_absolute_url(self):
		list_ = List.objects.create()
		self.assertEqual(list_.get_absolute_url(),'/lists/%d/' % (list_.id,))
