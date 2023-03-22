from django.shortcuts import render,redirect
from django.core import mail

from app01 import models
from app01.utils.form import AdminModelForm,AdminEditModelForm,AdminResetModelForm

def admin(request):
    if request.method == "GET":
        data = {}  # models.Admin.objects.filter的参数可以是字典
        value = request.GET.get('q', '')
        if value:
            data['username__contains'] = value
        admin_list = models.Admin.objects.filter(**data)
        return render(request, 'admin.html', {"admin_list": admin_list, "value": value})

def admin_add(request):
    context = {
        'title': '新增管理员',
        'back_url': '/admin/',
    }

    if request.method == 'GET':
        adminform = AdminModelForm()
        context['form']=adminform
        return render(request,'change.html',context)

    adminform = AdminModelForm(request.POST)
    if adminform.is_valid():
        adminform.save()
        # 管理员添加成功发送邮件
        mail.send_mail(subject='管理员添加',
                       message=f'管理员-{adminform.cleaned_data["username"]}成功添加',
                       from_email='945495541@qq.com',
                       recipient_list=['945495541@qq.com'])

        adminform = AdminModelForm()
        context['form'] = adminform
        context['flag'] = True
        return render(request,'change.html',context)

    context['form'] = adminform
    return render(request,'change.html',context)

def admin_edit(request,nid):
    """编辑管理员"""
    context = {
        'title': '编辑管理员',
        'back_url': '/admin/',
    }
    row_data = models.Admin.objects.filter(id=nid).first()
    if row_data is None:
        return render(request,'error.html',{'errmsg':'数据错误'})

    if request.method == 'GET':
        adminform = AdminEditModelForm(instance=row_data)
        context['form'] = adminform
        return render(request,'change.html',context)

    adminform = AdminEditModelForm(request.POST,instance=row_data)
    if adminform.is_valid():
        adminform.save()
        context['flag'] = True
        context['form'] = adminform
        return render(request,'change.html',context)

    context['form'] = adminform
    return render(request,'change.html',context)

def admin_delete(request,nid):
    '''删除管理员'''
    if models.Admin.objects.filter(id=nid):
        models.Admin.objects.filter(id=nid).delete()
        return redirect('/admin/')
    else:
        return render(request,'error.html',{'errmsg':'数据错误'})

def admin_reset(request,nid):
    '''重置管理员密码'''
    context = {
        'title': '重置密码',
        'back_url': '/admin/',
    }
    row_data = models.Admin.objects.filter(id=nid).first()
    if row_data is None:
        return render(request, 'error.html', {'errmsg': '数据错误'})

    if request.method == 'GET':
        adminform = AdminResetModelForm(instance=row_data)
        context['form'] = adminform
        return render(request,'change.html',context)

    adminform = AdminResetModelForm(request.POST,instance=row_data)
    if adminform.is_valid():
        adminform.save()
        context['flag'] = True
        context['form'] = adminform
        return render(request,'change.html',context)

    context['form'] = adminform
    return render(request,'change.html',context)


