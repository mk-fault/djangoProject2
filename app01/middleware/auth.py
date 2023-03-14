from django.shortcuts import redirect,render
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