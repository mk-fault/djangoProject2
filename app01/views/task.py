from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.form import TaskModelForm


@csrf_exempt
def task(request):
    if request.method == 'GET':
        form = TaskModelForm()
        return render(request,'task.html',{'form':form})

    print(request.POST)
    form = TaskModelForm(request.POST)
    if form.is_valid():
        form.save()
        data = {
            'status':True
        }
        return JsonResponse(data)

    data = {
        'status':False,
        'error':form.errors
    }
    return JsonResponse(data)