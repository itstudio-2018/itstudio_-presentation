from django.contrib import admin
from . import models


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'info', 'is_alive')
    ordering = ('is_alive',)
    list_filter = ('is_alive',)


@admin.register(models.Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'info')
    list_filter = ('year',)
    ordering = ('-year',)


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'get_department')
    list_filter = ('year', 'department')
    search_fields = ('name',)
    ordering = ('-year',)


@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'reply')
    ordering = ('-time',)
    list_per_page = 30
    list_editable = ['reply']
