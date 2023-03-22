import traceback

from django.core import mail
from django.conf import settings
from django.shortcuts import redirect,render,HttpResponse
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleWare(MiddlewareMixin):
    """自定义中间件，实现未登录无法访问的功能"""
    def process_request(self,request):
        if request.path_info in ["/login/","/login/code/"]:
            return
        info_dict =  request.session.get('info')
        if info_dict:
            return
        return redirect("/login/")

    def process_response(self,request,response):
        return response

class ExceptionMailMiddleWare(MiddlewareMixin):
    """将视图函数中的报错以邮件形式发送"""
    def process_exception(self,request,exception):
        mail.send_mail(subject='错误信息',
                       message=traceback.format_exc(),
                       from_email='945495541@qq.com',
                       recipient_list=settings.EX_EMAIL_RECIPIENT)
        return HttpResponse('页面错误')