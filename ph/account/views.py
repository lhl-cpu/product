from django.shortcuts import render,redirect
from django.contrib.auth.models import User #注册
from django.contrib import auth #登录
# Create your views here.


def signin(request):
	if request.method == 'GET':
		return render(request,'sign.html')
	elif request.method == 'POST':
		user_name = request.POST['用户名']
		password = request.POST['密码']
		passwordagain = request.POST['确认密码']
		try:
			User.objects.get(username=user_name)
			return render(request,'sign.html',{'用户名错误':'用户名已经存在'})
		except User.DoesNotExist:
			if password == passwordagain:
				User.objects.create_user(username=user_name,password=password)
				return redirect('主页')
			else:
				return render(request,'sign.html',{'密码错误':'两次密码不一致'})


def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	elif request.method == 'POST':
		user_name = request.POST['用户名']
		password = request.POST['密码']
		user = auth.authenticate(username=user_name,password=password)
		if user is None:
			return render(request,'login.html',{'信息错误':'请输入正确的用户名和密码！'})
		else:
			auth.login(request, user)
			return redirect('主页')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('主页')