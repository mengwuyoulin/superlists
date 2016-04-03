from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
#给Item类提供save方法，也为了让这个类编程真正的Django模型，要让它继承Model类
#继承models.Model的类映射到数据库中的一个表。默认情况下，这种类型会得到一个自动生成的ID属性作为表主键
#但其他列都要自行定义

class List(models.Model):
	def get_absolute_url(self):
		return reverse('view_list',args=[self.id])

class Item(models.Model):
	text = models.TextField(default='')
	list = models.ForeignKey(List,default=None)

	class Meta:
		ordering = ('id',)
		unique_together = ('list','text')

	def __str__(self):
		return self.text