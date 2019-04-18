from django.contrib import admin
from . import models


@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'year', 'status')
    list_per_page = 30
    search_fields = ('name',)
    list_filter = ('status', 'year')
    ordering = ('name', 'status')

    def status_1(self, request, queryset):
        queryset.update(status=1)
    status_1.short_description = '激活'

    def status_2(self, request, queryset):
        queryset.update(status=2)
    status_2.short_description = '通过初审'

    def status_3(self, request, queryset):
        queryset.update(status=3)
    status_3.short_description = '通过面试'

    def status_4(self, request, queryset):
        queryset.update(status=4)
    status_4.short_description = '选中'

    def status_false(self, request, queryset):
        queryset.update(status=-1)
    status_false.short_description = '刷下'

    actions = [status_1, status_2, status_3, status_4]


@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('email', 'expiration')
    list_per_page = 30
    ordering = ('expiration',)
    search_fields = ('email',)
