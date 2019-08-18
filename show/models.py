from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'部门名称')
    info = models.CharField(max_length=1000, verbose_name=u'介绍')
    is_alive = models.BooleanField(default=True, verbose_name=u'状态')

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Story(models.Model):
    year = models.IntegerField(verbose_name=u'年份')
    title = models.CharField(max_length=30, verbose_name=u'标题')
    info = models.CharField(max_length=100, verbose_name=u'介绍')

    class Meta:
        verbose_name = u'大事记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_year(self):
        return self.year

    def get_title(self):
        return self.title

    def get_info(self):
        return self.info


class Member(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'姓名')
    department = models.ForeignKey(Department, verbose_name=u'部门')
    year = models.IntegerField(verbose_name=u'年级')
    image = models.ImageField(verbose_name=u'图片', upload_to='')
    info = models.CharField(max_length=100, verbose_name=u'介绍')

    class Meta:
        verbose_name = u'成员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_department(self):
        return self.department.name
    get_department.short_description = '部门'


class Work(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'名称')
    image = models.ImageField(verbose_name=u'图片')
    url = models.URLField(verbose_name=u'网址')

    class Meta:
        verbose_name = u'作品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.CharField(max_length=100, verbose_name=u'内容')
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'留言时间')
    reply = models.CharField(max_length=100, blank=True, verbose_name=u'回复')

    class Meta:
        verbose_name = u'留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content






