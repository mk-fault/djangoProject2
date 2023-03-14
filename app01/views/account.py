from io import BytesIO

from django.shortcuts import render,redirect,HttpResponse

from app01.models import Admin
from app01.utils.form import LoginForm
from app01 import models
from app01.utils.gen_code import check_code

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html',{'form':form})

    form = LoginForm(request.POST)
    if form.is_valid():
        # 验证码校验
        ori_code = request.session.get('verify','')
        user_code = form.cleaned_data.pop('verify')  # 后续验证中form应该把verify字段去掉
        if ori_code.upper() != user_code.upper():
            form.add_error('verify','验证码输入错误')
            return render(request,'login.html',{'form':form})

        # 验证用户名密码
        obj = models.Admin.objects.filter(**form.cleaned_data).first()
        # 数据库中不存在则返回登录界面并报错
        if obj is None:
            form.add_error('password',"用户名或密码错误")
            return render(request,'login.html',{'form':form})

        request.session['info'] = {'id':obj.id,'username':obj.username}
        request.session.set_expiry(60*60*24*7)
        return redirect('/index/')

    return render(request,'login.html',{'form':form})

def logout(request):
    request.session.clear()
    return redirect('/login/')

def get_code(request):
    img,code = check_code()

    request.session['verify'] = code
    request.session.set_expiry(60)

    stream = BytesIO()       # 用BytesIO在内存中生成对象，用于保存验证码图片，就不用反复访问硬盘
    img.save(stream,'PNG')
    return HttpResponse(stream.getvalue())
