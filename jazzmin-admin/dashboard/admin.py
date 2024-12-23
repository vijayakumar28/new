from django.contrib import admin
from dashboard.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'employee_id', 'department', 'position', 'date_of_joining')
    search_fields = ('full_name', 'employee_id', 'department')

admin.site.register(Employee, EmployeeAdmin)
