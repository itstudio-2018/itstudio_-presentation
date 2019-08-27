from django.contrib import admin
from . import models
from django.http import StreamingHttpResponse
import xlwt
from .views import sent_status
import logging
info_log = logging.getLogger('info')


@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'year', 'status', 'get_department')
    list_per_page = 30
    search_fields = ('name',)
    list_filter = ('status', 'year', 'department')
    ordering = ('name', '-status')

    def status_1(self, request, queryset):
        queryset = queryset.filter(status=0)
        info_log.info("send_email_status_1")

        email = []
        for one in queryset:
            email.append(str(one.email))
        sent_status(email, 1)

        queryset.update(status=1)
    status_1.short_description = '未激活 --> 已激活'

    def status_2(self, request, queryset):
        queryset = queryset.filter(status=1)
        info_log.info("send_email_status_2")

        email = []
        for one in queryset:
            email.append(str(one.email))
        sent_status(email, 2)

        queryset.update(status=2)
    status_2.short_description = '已激活 --> 未通过初审'

    def status_3(self, request, queryset):
        queryset = queryset.filter(status=1)
        info_log.info("send_email_status_3")

        email = []
        for one in queryset:
            email.append(str(one.email))
        sent_status(email, 3)

        queryset.update(status=3)
    status_3.short_description = '已激活 --> 已通过初审'

    def status_4(self, request, queryset):
        queryset = queryset.filter(status=3)
        info_log.info("send_email_status_4")

        email = []
        for one in queryset:
            email.append(str(one.email))
        sent_status(email, 4)

        queryset.update(status=4)
    status_4.short_description = '已通过初审 --> 未通过面试'

    def status_5(self, request, queryset):
        queryset = queryset.filter(status=3)
        info_log.info("send_email_status_5")

        email = []
        for one in queryset:
            email.append(str(one.email))
        sent_status(email, 5)

        queryset.update(status=5)
    status_5.short_description = '已通过初审 --> 已通过面试'

    def status_6(self, request, queryset):
        queryset = queryset.filter(status=5)
        info_log.info("send_email_status_6")

        email = []
        for one in queryset:
            email.append(str(one.email))
        sent_status(email, 6)

        queryset.update(status=6)
    status_6.short_description = '已通过面试 --> 未通过笔试'

    def status_7(self, request, queryset):
        queryset = queryset.filter(status=5)
        info_log.info("send_email_status_7")

        email = []
        for one in queryset:
            email.append(str(one.email))
        sent_status(email, 7)

        queryset.update(status=7)
    status_7.short_description = '已通过面试 --> 已通过笔试'

    def status_8(self, request, queryset):
        queryset = queryset.filter(status=7)
        info_log.info("send_email_status_8")

        email = []
        for one in queryset:
            email.append(str(one.email))
        sent_status(email, 8)

        queryset.update(status=8)
    status_8.short_description = '已通过笔试 --> 未录取'

    def status_9(self, request, queryset):
        queryset = queryset.filter(status=7)
        info_log.info("send_email_status_9")

        email = []
        for one in queryset:
            email.append(str(one.email))
        sent_status(email, 9)

        queryset.update(status=9)
    status_9.short_description = '已通过笔试 --> 已录取'

    def save_excel(self, request, queryset):
        filename = 'information'
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('main')

        all_information = models.Applicant.objects.all()

        worksheet.write(0, 0, label='姓名')
        worksheet.col(0).width = 5000
        worksheet.write(0, 1, label='手机号')
        worksheet.col(1).width = 5000
        worksheet.write(0, 2, label='邮箱')
        worksheet.col(2).width = 5000
        worksheet.write(0, 3, label='年级')
        worksheet.write(0, 4, label='学院')
        worksheet.write(0, 5, label='专业')
        worksheet.write(0, 6, label='状态')
        worksheet.write(0, 7, label='意向部门')

        i = 1
        for one in all_information:
            worksheet.write(i, 0, label=one.name)
            worksheet.write(i, 1, label=one.phone_number)
            worksheet.write(i, 2, label=one.email)
            worksheet.write(i, 3, label=one.year)
            worksheet.write(i, 4, label=one.college)
            worksheet.write(i, 5, label=one.speciality)
            worksheet.write(i, 6, label=one.status)
            worksheet.write(i, 7, label=one.department.name)

            i = i + 1

        workbook.save("%s" % filename)

        def file_iterator(filename, chunk_size=512):
            with open(filename, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        response = StreamingHttpResponse(file_iterator(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="{}" '.format("Result.xls")
        return response
    save_excel.short_description = '导入Excel表格'

    actions = [status_1, status_2, status_3, status_4, status_5, status_6, status_7, status_8, status_9,
               save_excel]


@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('email', 'expiration')
    list_per_page = 30
    ordering = ('expiration',)
    search_fields = ('email',)
