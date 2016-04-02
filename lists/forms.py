from django import forms
from lists.models import Item

EMPTY_LIST_ERROR = "不能输入空事项"

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