from django.db import models

# Create your models here.

# 部门表
class Department(models.Model):
    title = models.CharField(verbose_name='部门名称',max_length=32,unique=True)

    def __str__(self):
        """如果不加这一行，人员添加时选择部门则会显示成对象"""
        return self.title

# 员工表
class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateField(verbose_name='入职时间')
    depart = models.ForeignKey(verbose_name='所属部门',to='Department',to_field='id',on_delete=models.CASCADE,related_name='users')

    gender_choices = ((1,'男'),(2,'女'))

    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)

    def __str__(self):
        return self.name

# 靓号表
class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name='手机号',max_length=11)
    price = models.IntegerField(verbose_name='价格')

    lever_choice = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级'),
        (5, '五级'),
    )
    level = models.SmallIntegerField(verbose_name='级别',choices=lever_choice,default=1)
    status_choice = (
        (1,'已占用'),
        (2,'未使用')
    )
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choice,default=2)

# 管理员表
class Admin(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)

    def __str__(self):
        return self.username


# 任务表
class Task(models.Model):
    title = models.CharField(verbose_name='项目名',max_length=64)
    level_choice = (
        (1,'非常紧急'),
        (2,'紧急'),
        (3,'重要'),
        (4,'一般')
    )
    level = models.SmallIntegerField(verbose_name='级别',choices=level_choice,default=4)
    detail = models.TextField(verbose_name='详细描述')
    manager = models.ForeignKey(verbose_name='负责人',to='UserInfo',to_field='id',on_delete=models.CASCADE)

# 订单表
class Order(models.Model):
    oid = models.CharField(verbose_name='订单号',max_length=64)
    title = models.CharField(verbose_name='商品名',max_length=64)
    price = models.IntegerField(verbose_name='价格')

    status_choice = (
        (1,'已支付'),
        (2,'未支付')
    )
    status = models.SmallIntegerField(verbose_name='支付状态',choices=status_choice,default=2)
    admin = models.ForeignKey(verbose_name='管理员',to='Admin',on_delete=models.CASCADE)