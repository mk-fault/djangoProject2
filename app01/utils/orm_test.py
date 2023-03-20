import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject2.settings")

import django
django.setup()

from app01 import models

# range - id在(1,3)范围中的
res = models.Department.objects.filter(id__range=[1,3])
# in - id为1或3的
res = models.Department.objects.filter(id__in=[1,3])
# contain - 子串查询
res = models.Department.objects.filter(title__contains='部')
# icontain - 同上，忽略大小写
res = models.Department.objects.filter(title__icontains='部')
# year - 筛选时间
res = models.UserInfo.objects.filter(create_time__year='2019')

# 通过外键，反向拿取一对多的关联对象
res = models.Department.objects.filter(title='法务部').first()
# print(res.userinfo_set.all()) # 未指定related_name时调用
# print(res.users.all())        # 指定了related_name时调用
res = models.UserInfo.objects.filter(depart__title='法务部') # 外键字段加上__后跟外表字段，则可以实现上面两句查询的效果
res = models.Department.objects.filter(users__name='LCH')
# print(res)

# 聚合函数，求和、最大、最小、平均等，可同时聚合多个字段
from django.db.models import Avg,Max,Min,Sum,F,Q
res = models.UserInfo.objects.all().aggregate(Avg('account'),Max('age'))

# 分组，查看各部门的最高工资
res = models.UserInfo.objects.values('depart__title').annotate(Max('account'))

# F查询
res = models.UserInfo.objects.filter(account__gt=F('age'))  # => where account > age
# F更新，获取数据库中之前保存的值
models.UserInfo.objects.filter(id__lte=4).update(age=F('age') * 2)
# Q查询，逻辑查询，用Q()包裹语句，并用|、&、~相连
# | 或
# & 与
# ~ 非
res = models.UserInfo.objects.filter(Q(id__lte=4)|Q(id__gte=6))
# print(res)
