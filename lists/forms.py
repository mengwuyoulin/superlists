from django import forms
from lists.models import Item
from django.core.exceptions import ValidationError

EMPTY_LIST_ERROR = "待办事项不能为空"
DUPLICATE_ITEM_ERROR = "你已经添加过此事项！"

class ItemForm(forms.models.ModelForm):

	class Meta:
		model = Item
		fields = ('text',)
		widgets={
			'text':forms.fields.TextInput(attrs={
				'placeholder':'请输入任务名称',
				'class':'form-control input-lg',
			}),
		}
		error_messages = {
			'text':{'required':EMPTY_LIST_ERROR}
		}

	def save(self,for_list):
		self.instance.list = for_list #.instance属性：修改或创建数据库的对象
		return super().save()

class ExistingListItemForm(ItemForm):
	"""docstring for ExistingListItemForm"""
	def __init__(self, for_list,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.instance.list = for_list

	def validate_unique(self):
		try:
			self.instance.validate_unique()
		except ValidationError as e:
			e.error_dict = {'text':[DUPLICATE_ITEM_ERROR]}
			self._update_errors(e)

	def save(self):
		return forms.models.ModelForm.save(self)
		