from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from app01.utils.form import UserModelForm,MobileModelForm,MobileEditModelForm

# ------------------------靓号管理----------------------------
def mobile(request):
    if request.method == "GET":
        data = {}
        value = request.GET.get('num','')
        if value:
            data['mobile__contains'] = value
        mobile_list = models.PrettyNum.objects.filter(**data)
        return render(request,'mobile.html',{"mobile_list":mobile_list,"value":value})


def mobile_add(request):
    if request.method == "GET":
        form = MobileModelForm()
        return render(request,'mobile_add.html',{"form":form})

    form = MobileModelForm(request.POST)
    if form.is_valid():
        form.save()
        form = MobileModelForm()
        flag = True
        return render(request,'mobile_add.html',{"form":form,"flag":flag})

    return render(request,'mobile_add.html',{"form":form})


def mobile_edit(request,nid):
    row_obj = models.PrettyNum.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = MobileEditModelForm(instance=row_obj)
        return render(request,'mobile_edit.html',{'form':form})

    form = MobileEditModelForm(request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        flag = True
        return render(request,'mobile_edit.html',{"flag":flag,"form":form})

    return render(request,'mobile_edit.html',{"form":form})

def mobile_delete(request,nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/mobile/')