from django.contrib import admin
from .models import Student
class StudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone','qq', 'is_enroll','institute','major','obj_school','modifed_date']
	search_fields =('name','phone','qq','major','institute')
	list_filter =('is_enroll','modifed_date',)
	ordering = ('-modifed_date',)
admin.site.site_header = '文都考研后台系统'
admin.site.site_title = '学生数据'
admin.site.index_title = '管理'
admin.site.register(Student,StudentAdmin)
# Register your models here.
