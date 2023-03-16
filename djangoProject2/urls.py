"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# 想要使用Media目录需配置re_path,settings,serve
from django.urls import path,re_path,include
from django.conf import settings
from django.views.static import serve

import app01
from app01.views import department,index,mobile,user,account,task,order,graph
from app01.views import admin as adm

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},name='media'),
    # path("admin/", admin.site.urls),
    path("index/",index.index),

    # 部门管理
    path("department/",department.department),
    path("department/add/",department.depart_add),
    path("department/delete/",department.depart_delete),
    path("department/<int:nid>/edit",department.depart_edit),
    path("department/class/",department.depart_class.as_view()),
    path("app01/",include('app01.urls')),   # 分体路由，将后续URL交于app01下的urls.py绑定

    # 用户管理
    path("user/",user.user),
    path("user/add/",user.user_add),
    path("user/add_modelform/",user.user_add_modelform),
    path("user/<int:nid>/edit",user.user_edit),
    path("user/<int:nid>/delete",user.user_delete),

    # 靓号管理
    path("mobile/",mobile.mobile),
    path("mobile/add/",mobile.mobile_add),
    path("mobile/<int:nid>/edit/",mobile.mobile_edit),
    path("mobile/<int:nid>/delete/",mobile.mobile_delete),
    path("mobile/multiadd/",mobile.mobile_multiadd),

    # 管理员管理
    path("admin/",adm.admin),
    path("admin/add/",adm.admin_add),
    path("admin/<int:nid>/edit/",adm.admin_edit),
    path("admin/<int:nid>/delete/",adm.admin_delete),
    path("admin/<int:nid>/reset/",adm.admin_reset),

    # 用户登录
    path("login/",account.login),
    path("",account.login),
    path("logout/",account.logout),
    path("login/code/",account.get_code),

    # 任务管理
    path("task/ajax/",task.task_ajax),
    path("task/",task.task),

    # 订单管理
    path("order/",order.order),
    path("order/add/",order.order_add),
    path("order/delete/",order.order_delete),
    path("order/edit/show/",order.order_edit_show),
    path("order/edit/",order.order_edit),

    # 数据分析
    path("graph/",graph.graph),
    path("graph/data/",graph.graph_data)
]
