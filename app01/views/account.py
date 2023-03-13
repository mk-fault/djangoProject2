from django.shortcuts import render,redirect

from app01.models import Admin
from app01.utils.form import LoginForm
from app01 import models

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html',{'form':form})

    form = LoginForm(request.POST)
    if form.is_valid():
        obj = models.Admin.objects.filter(**form.cleaned_data).first()

        # 数据库中不存在则返回登录界面并报错
        if obj is None:
            form.add_error('password',"用户名或密码错误")
            return render(request,'login.html',{'form':form})

        request.session['info'] = {'id':obj.id,'username':obj.username}
        return redirect('/index/')

    return render(request,'login.html',{'form':form})

def logout(request):
    request.session.clear()
    return redirect('/login/')