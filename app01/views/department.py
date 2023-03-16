from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from app01 import models
from app01.utils.form import UserModelForm,MobileModelForm,MobileEditModelForm


# ------------------------部门管理----------------------------
def department(request):
    depart_list = models.Department.objects.all().order_by('id')
    # print(depart_list.values())
    #<QuerySet [{'id': 1, 'title': '销售部'}, {'id': 2, 'title': '后勤部'}, {'id': 3, 'title': '财务部'}, {'id': 4, 'title': '法务部'}, {'id': 10, 'title': '文化部'}]>
    # for遍历，就能得到每个字典，数据库字段名作为键,values中若填入参数，则只会返回所填字段的数据
    # print(depart_list.values('title'))
    # < QuerySet[{'title': '销售部'}, {'title': '后勤部'}, {'title': '财务部'}, {'title': '法务部'}, {'title': '文化部'}] >
    # depart_list.values_list() :返回[(),()]，每个元组装有一整条数据，不含字段名
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
    # models.Department.objects.exclude(id=xx)取反
    return redirect('/department/')

def depart_edit(request,nid):
    if request.method == 'GET':
        obj = models.Department.objects.filter(id=nid).first()
        return render(request,'depart_edit.html',{'obj':obj})

    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/department/')


# 使用类的方法定义视图(CBV)
class depart_class(View):
    def get(self,request):
        depart_list = models.Department.objects.all().order_by('id')
        return render(request, 'department.html', {'depart_list': depart_list})
