from django import forms
from lists.models import Item

EMPTY_LIST_ERROR = "待办事项不能为空"

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