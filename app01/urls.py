from django.urls import path
from app01.views import department

urlpatterns = [
    path('ftly/',department.depart_class.as_view()) #分体路由
]