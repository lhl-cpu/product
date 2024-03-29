from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.

def home(request):
	products = Product.objects
	return render(request,'home.html',{'products':products})

def detail(request,product_id):
	product = get_object_or_404(Product,pk=product_id)
	return render(request,'detail.html',{'product': product})

@login_required
def publish(request):
	if request.method == 'GET':
		return render(request,'publish.html')
	elif request.method == 'POST':
		title = request.POST['标题']
		text = request.POST['介绍']
		url = request.POST['App链接']
		try:
			icno = request.FILES['App图标']

			product = Product()
			product.title = title
			product.text = text
			product.url = url
			product.icno = icno

			product.pub_date = timezone.datetime.now()
			product.hunter = request.user

			product.save()

			return redirect('主页')
		except Exception as err:
			return render(request,'publish.html',{'错误':'请上传图片！'})