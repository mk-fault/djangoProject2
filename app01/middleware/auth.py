from django.shortcuts import redirect,render
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        if request.path_info == "/login/":
            return
        info_dict =  request.session.get('info')
        if info_dict:
            return
        return redirect("/login/")

    def process_response(self,request,response):
        return response