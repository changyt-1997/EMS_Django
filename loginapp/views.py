from django.shortcuts import render,HttpResponse,redirect
from loginapp.models import User
# Create your views here.


def login(request):
    n = request.COOKIES.get('name')
    p = request.COOKIES.get('pwd')
    result = User.objects.filter(username=n,password=p)
    if result:
        request.session['login']='ok'
        return redirect('employeeapp:home')
    return render(request,'login.html')

def judge_login(request):
    n_name = request.POST.get('name')
    n_pwd = request.POST.get('pwd')
    n_rem = request.POST.get('remember')
    result = User.objects.filter(username=n_name,password=n_pwd)
    if result:
        response = redirect('employeeapp:home')
        request.session['login']='ok'
        if n_rem:
            #验证用户有没有勾选免登录，如果勾选了储存cookie到浏览器
            response.set_cookie('name',n_name,max_age=7*24*3600)
            response.set_cookie('pwd',n_pwd,max_age=7*24*3600)
        # render(request,'')
        return response
    return HttpResponse('登录失败')


def regist(request):
    return render(request,'regist.html')


def judge_regist(request):
    new_username = request.POST.get('username')
    new_name = request.POST.get('name')
    new_pwd = request.POST.get('pwd')
    new_sex = request.POST.get('sex')
    result = User.objects.filter(username=new_username)
    if result:
        return HttpResponse('注册失败！')
    User.objects.create(username=new_username,name=new_name,password=new_pwd,sex=new_sex)
    return redirect('loginapp:judge_re')


def hello():
    print('ss')
    print('ss')
    print('ss')
    print('ss')
    return 555

# def emplist(request):
# #     result = request.session.get('login')
# #     if result:
# #         return render(request,'emplist.html')
# #     return redirect('loginapp:login')