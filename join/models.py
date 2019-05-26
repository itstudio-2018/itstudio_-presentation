from django.db import models
from show.models import Department


class Applicant(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    phone_number = models.CharField(max_length=11, unique=True, verbose_name=u'手机号')
    email = models.EmailField(max_length=254, unique=True, verbose_name=u'邮箱')
    year = models.IntegerField(verbose_name=u'年级')
    college = models.CharField(max_length=20, verbose_name=u'学院')
    speciality = models.CharField(max_length=20, verbose_name=u'专业')
    department = models.ForeignKey(Department, verbose_name=u'意向部门')
    message = models.CharField(max_length=200, verbose_name=u'备注', default='', blank=True)

    status_choice = (
        (-1, '未通过'),
        (0, '未激活'),
        (1, '待初审'),
        (2, '待面试'),
        (3, '待笔试'),
        (4, '已选中'),
    )

    status = models.SmallIntegerField(default=0, choices=status_choice, verbose_name=u'状态')

    class Meta:
        verbose_name = u'申请人'
        verbose_name_plural = verbose_name

        ordering = ['-status', 'name']

    def __str__(self):
        return self.name


class Link(models.Model):
    email = models.EmailField(max_length=254, unique=True, verbose_name=u'邮箱')
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    expiration = models.DateTimeField(auto_now_add=True, verbose_name=u'过期时间')

    class Meta:
        verbose_name = u'激活链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email

