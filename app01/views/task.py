from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01 import models
from app01.utils.form import TaskModelForm



def task(request):
    form = TaskModelForm()
    task_list = models.Task.objects.all()
    context = {
        'form': form,
        'task_list':task_list
    }
    return render(request, 'task.html', context)


@csrf_exempt
def task_ajax(request):
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