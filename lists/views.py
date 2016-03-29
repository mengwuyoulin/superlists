from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from lists.models import Item

@csrf_exempt# Create your views here.
def home_page(request):
	#new_item_text是POST请求中的数据，或者空字符串
	if request.method == 'POST':
		#.objects.create是创建新Item对象的简化方式，无需调用.save()
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	items = Item.objects.all()
	return render(request,'home.html',{'items':items})

def view_list(request):
	items = Item.objects.all()
	return render(request,'home.html',{'items':items})