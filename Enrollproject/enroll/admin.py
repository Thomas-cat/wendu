from django.contrib import admin
from .models import Student,Student2,YuBaoMing

class StudentAdmin2(admin.ModelAdmin):
	list_display = ['name','sex','phone','qq', 'is_enroll','is_return','ride_date','ride_time','price','is_need','major','obj_school','obj_major','modifed_date']
	search_fields =('name','phone','qq','major','is_enroll','obj_school','obj_major')
	list_filter =('ride_date','ride_time','is_enroll',)
	list_per_page = 50
	ordering = ('-modifed_date',)
class YuBaoMingAdmin(admin.ModelAdmin):
	list_display = ['name','phone','major','area','need_dorm','need_bus','need_lunch']
	list_per_page = 50
	ordering = ('-modifed_date',)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone','qq', 'is_enroll','institute','major','obj_school','modifed_date']
	search_fields =('name','phone','qq','major','institute')
	list_filter =('is_enroll','modifed_date',)
	list_per_page = 50
	ordering = ('-modifed_date',)
admin.site.site_header = '文都考研后台系统'
admin.site.site_title = '学生数据'
admin.site.index_title = '管理'
admin.site.register(Student,StudentAdmin)
admin.site.register(Student2,StudentAdmin2)
admin.site.register(YuBaoMing,YuBaoMingAdmin)
# Register your models here.
