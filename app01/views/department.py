from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from app01.utils.form import UserModelForm,MobileModelForm,MobileEditModelForm


# ------------------------部门管理----------------------------
def department(request):
    depart_list = models.Department.objects.all().order_by('id')
    return render(request,'department.html',{'depart_list':depart_list})

def depart_add(request):
    if request.method == 'GET':
        return render(request,'depart_add.html')

    title = request.POST.get('title')
    models.Department.objects.create(title=title)
    flag = True
    return render(request,'depart_add.html',{'flag':flag})

def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/department/')

def depart_edit(request,nid):
    if request.method == 'GET':
        obj = models.Department.objects.filter(id=nid).first()
        return render(request,'depart_edit.html',{'obj':obj})

    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/department/')

