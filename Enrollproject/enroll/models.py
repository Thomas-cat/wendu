from django.db import models
class Student(models.Model):
	name = models.CharField(max_length = 20,verbose_name='姓名',blank=False)
	qq = models.CharField(max_length = 12,blank=True)
	obj_school = models.CharField(max_length = 100,verbose_name = '目标学校')
	institute = models.CharField(max_length = 100,verbose_name = '所在学院')
	major = models.CharField(max_length = 100,blank=True,verbose_name = '所在专业')
	phone = models.CharField(max_length=11,blank=False,verbose_name = '手机号')
	is_enroll = models.BooleanField(blank=True,verbose_name = '是否学员')
	modifed_date = models.DateTimeField(auto_now_add=True,verbose_name ='信息提交时间')
	class Meta:
		 verbose_name_plural='学生报名信息表'
