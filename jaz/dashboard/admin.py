from django.contrib import admin
from dashboard.models import Employee, Comment

from unfold.admin import ModelAdmin as unfoldModelAdmin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'message')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'employee_id', 'department', 'position', 'date_of_joining')
    search_fields = ('full_name', 'employee_id', 'department')
    list_filter = ('employment_type', 'gender')
