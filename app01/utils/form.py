import re

from django import forms
from django.shortcuts import render,redirect,HttpResponse
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from app01 import models
from app01.utils.encrypt import MD5


# 写一个Bootsrap的类，改写其init方法，让后面的ModelForm都继承他，就可以为Django自动生成的HTML加上CSS样式
class Bootstrap:
    def __init__(self,*args,**kwargs):
        super().__init__( *args,**kwargs) # 我敲，必须吧*args和 **kwargs加上，不然POST传回时没有值
        for name,field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {"class":"form-control",
                                      "placeholder":field.label}

class BootstrapModelForm(Bootstrap,forms.ModelForm):
    # def __init__(self,*args,**kwargs):
    #     super(BootstrapModelForm, self).__init__( *args,**kwargs) # 我敲，必须吧*args和 **kwargs加上，不然POST传回时没有值
    #     for name,field in self.fields.items():
    #         if field.widget.attrs:
    #             field.widget.attrs['class'] = "form-control"
    #             field.widget.attrs['placeholder'] = field.label
    #         else:
    #             field.widget.attrs = {"class":"form-control",
    #                                   "placeholder":field.label}
    pass

class BootstrapForm(Bootstrap,forms.Form):
    pass

# 用户管理ModelForm
class UserModelForm(BootstrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name','password','age','account','create_time','gender','depart']

# 靓号管理
class MobileModelForm(BootstrapModelForm):
    # 验证手机号，方法一：validators
    # mobile = forms.CharField(
    #     # label = '手机号',
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')]
    # )

    class Meta:
        model = models.PrettyNum
        fields = "__all__"

    # def __init__(self):
    #     super(MobileModelForm, self).__init__()
    #     self.fields['mobile'].validators = [RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]


    # 方法二：钩子方法验证，要求字段已在Meta中添加
    # 在钩子方法中可以通过self.instance.pk获取当前数据的primary key值(id)
    def clean_mobile(self):
        _mobile = self.cleaned_data['mobile']

        if re.match(r'^1[3-9]\d{9}$',_mobile) is None:
            raise ValidationError("手机号格式错误")

        exist = models.PrettyNum.objects.filter(mobile=_mobile).exists()
        if exist:
            raise ValidationError("手机号已存在")

        return _mobile

#继承后修改mobile字段不能显示
class MobileEditModelForm(MobileModelForm):

    mobile = forms.CharField(disabled=True,label='手机号')

    # 若可改手机号，需要验证数据库中已有的手机号是否就是当前修改的手机号（编辑但手机号不变的情况）
    # def clean_mobile(self):
    #     _mobile = self.cleaned_data['mobile']
    #     exist = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=_mobile).exists()   # self.instance.pk 即primary key->ID
    #     if exist:
    #         raise ValidationError('手机号已存在')
    #     return _mobile

class AdminModelForm(BootstrapModelForm):
    confirm = forms.CharField(max_length=64,label='确认密码',widget=forms.PasswordInput)

    class Meta:
        model = models.Admin
        fields = ['username','password','confirm']   # 新增字段也要在field中添加上
        widgets = {
            'password':forms.PasswordInput
        }

    def clean_password(self):
        _password = self.cleaned_data['password']
        return MD5(_password)

    def clean_confirm(self):
        _confirm = self.cleaned_data['confirm']
        md5_confirm = MD5(_confirm)
        md5_password = self.cleaned_data['password']
        if md5_confirm != md5_password:
            raise ValidationError("密码不一致")
        return md5_confirm

class AdminEditModelForm(AdminModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']

class AdminResetModelForm(AdminModelForm):
    username = forms.CharField(label='用户名',disabled=True,max_length=32)

    # class Meta:
    #     model = models.Admin
    #     fields = ['username','password','confirm']   # 新增字段也要在field中添加上
    #     widgets = {
    #         'password':forms.PasswordInput
    #     }

class LoginForm(BootstrapForm):
    username = forms.CharField(label='用户名',widget=forms.TextInput,required=True)
    password = forms.CharField(label='密码',widget=forms.PasswordInput(render_value=True),required=True)
    verify = forms.CharField(label='验证码',widget=forms.TextInput,required=True)

    def clean_password(self):
        md5_pwd = MD5(self.cleaned_data['password'])
        return md5_pwd

class TaskModelForm(BootstrapModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'
        widgets = {
            'detail':forms.TextInput
        }

class OrderModelForm(BootstrapModelForm):
    class Meta:
        model = models.Order
        exclude = ['oid','admin']
