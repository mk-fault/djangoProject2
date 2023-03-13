from django.shortcuts import render,redirect
from app01 import models
from app01.utils.form import AdminModelForm

def admin(request):
    if request.method == "GET":
        data = {}
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
        adminform = AdminModelForm()
        context['form'] = adminform
        context['flag'] = True
        return render(request,'change.html',context)

    context['form'] = adminform
    return render(request,'change.html',context)

def admin_edit(request,nid):
    context = {
        'title': '编辑管理员',
        'back_url': '/admin/',
    }
    row_data = models.Admin.objects.filter(id=nid).first()

    if request.method == 'GET':
        adminform = AdminModelForm(instance=row_data)
        context['form'] = adminform
        return render(request,'change.html',context)

    adminform = AdminModelForm(request.POST,instance=row_data)
    if adminform.is_valid():
        adminform.save()
        context['flag'] = True
        context['form'] = adminform
        return render(request,'change.html',context)

    context['form'] = adminform
    return render(request,'change.html',context)

def admin_delete(request,nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/')