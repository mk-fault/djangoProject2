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
from django.urls import path

from app01.views import department,index,mobile,user,account,task
from app01.views import admin as adm

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("index/",index.index),

    # 部门管理
    path("department/",department.department),
    path("department/add/",department.depart_add),
    path("department/delete/",department.depart_delete),
    path("department/<int:nid>/edit",department.depart_edit),

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
    path("task/",task.task)
]
