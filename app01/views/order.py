import codecs
import random
import datetime
import csv

from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app01.utils.form import OrderModelForm
from app01 import models

# 主页面，显示订单信息和提供空的form表单给新增模态框
def order(request):
    order_list = models.Order.objects.all()

    form = OrderModelForm()
    context = {
        'form':form,
        'order_list':order_list
    }
    return render(request,'order.html',context)

# 订单增加，后台生成oid和admin
@csrf_exempt
def order_add(request):
    form = OrderModelForm(request.POST)
    print(type(request.POST))
    if form.is_valid():

        oid = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(10000,99999))
        form.instance.oid = oid
        form.instance.admin_id = request.session['info']['id']
        form.save()
        data = {
            'status':True
        }
        return JsonResponse(data)

    data = {
        'status':False,
        'errors':form.errors
    }
    return JsonResponse(data)

# 订单删除
@csrf_exempt
def order_delete(request):
    delete_id = request.POST.get('delete_id')
    if models.Order.objects.filter(id=delete_id).exists():
        models.Order.objects.filter(id=delete_id).delete()
        data = {
            'status':True
        }
    else:
        data = {
            'status':False
        }
    return JsonResponse(data)

# 为订单编辑页面提供原始数据
def order_edit_show(request):
    edit_id = request.GET.get('edit_id')
    edit_info = models.Order.objects.filter(id=edit_id).first()
    if edit_info:

        # 方法一，生成form后遍历取其name和value
        # eform = OrderModelForm(instance=edit_info)
        # dic = {}
        # for item in eform:
        #     dic[item.name] = item.value()

        # 方法二，通过.values直接获取字典形式的数据
        row_dic = models.Order.objects.filter(id=edit_id).values('title','price','status').first()
        data = {
            'status':True,
            'dic':row_dic
        }
        return JsonResponse(data)
    else:
        data = {
            'status':False
        }
        return JsonResponse(data)

# 订单编辑
@csrf_exempt
def order_edit(request):
    edit_id = request.GET.get('edit_id')
    obj = models.Order.objects.filter(id=edit_id).first()
    if not obj:
        data = {
            'exist': False
        }
        return JsonResponse(data)

    edit_form = OrderModelForm(request.POST,instance=obj)
    if edit_form.is_valid():
        edit_form.instance.oid = obj.oid
        edit_form.instance.admin_id = request.session['info']['id']
        edit_form.save()
        data = {
            'exist':True,
            'status':True
        }
        return JsonResponse(data)

    data = {
        'exist':True,
        'status':False,
        'errors':edit_form.errors
    }
    return JsonResponse(data)

#  订单下载
def order_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="order.csv'
    order_list = models.Order.objects.all()
    response.write(codecs.BOM_UTF8)  # 解决中文乱码问题！！！！！
    writer = csv.writer(response)
    title_list = ['ID','订单号','商品名','价格','状态','管理员']
    writer.writerow(title_list)
    for ord in order_list:
        writer.writerow([ord.id,ord.oid,ord.title,ord.price,ord.status,ord.admin])

    return response


