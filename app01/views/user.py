from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from app01.utils.form import UserModelForm,MobileModelForm,MobileEditModelForm

# ------------------------人员管理----------------------------
def user(request):
    user_list = models.UserInfo.objects.all().order_by('id')
    return render(request,'user.html',{'user_list':user_list})

def user_add(request):
    if request.method == 'GET':
        data_list = {
           "gender_choice" : models.UserInfo.gender_choices,
           "department_list" : models.Department.objects.all()
        }

        return render(request,'user_add.html',data_list)

    name = request.POST.get('name')
    password = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('account')
    create_time = request.POST.get('ctime')
    gender_id = request.POST.get('gender')
    depart_id = request.POST.get('department')

    models.UserInfo.objects.create(name=name,password=password,age=age,account=account,create_time=create_time,gender=gender_id,depart_id=depart_id)
    flag = True
    return render(request,'user_add.html',{'flag':flag})

# 使用modelform



def user_add_modelform(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request,'user_add_modelform.html',{"form":form})

    form = UserModelForm(request.POST)
    if form.is_valid():
        form.save()
        flag = True
        form = UserModelForm()
        return render(request,'user_add_modelform.html',{"flag":flag,"form":form})

    return render(request,'user_add_modelform.html',{"form":form})

def user_edit(request,nid):

    row_obj = models.UserInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = UserModelForm(instance=row_obj)
        return render(request,'user_edit.html',{'form':form})

    form = UserModelForm(request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        flag = True
        return render(request,'user_edit.html',{"flag":flag,"form":form})

    return render(request,'user_edit.html',{"form":form})

def user_delete(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/')