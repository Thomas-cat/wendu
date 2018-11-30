from django.db import models
class Student(models.Model):
	name = models.CharField(max_length = 20,verbose_name='姓名',blank=False)
	qq = models.CharField(max_length = 12,blank=True)
	obj_school = models.CharField(max_length = 100,verbose_name = '目标学校',blank=True)
	institute = models.CharField(max_length = 100,verbose_name = '所在学院',blank = True)
	major = models.CharField(max_length = 100,blank=True,verbose_name = '所在专业')
	phone = models.CharField(max_length=11,blank=False,verbose_name = '手机号')
	is_enroll = models.BooleanField(blank=True,verbose_name = '是否学员')
	modifed_date = models.DateTimeField(auto_now_add=True,verbose_name ='信息提交时间')
	class Meta:
		 verbose_name_plural='文都直通车'
	def __str__(self):	 	
		return self.name
class YuBaoMing(models.Model):
	name = models.CharField(max_length = 20,verbose_name='姓名',blank=False)
	phone = models.CharField(max_length=11,blank=False,verbose_name = '手机号')
	modifed_date = models.DateTimeField(auto_now_add=True,verbose_name ='提交时间')
	need_bus = models.CharField(max_length = 4,blank=False,verbose_name = '大巴车')
	lunch_choice = (('是','是'),('否','否'))
	need_lunch = models.CharField(max_length = 10,blank=True,choices=lunch_choice,verbose_name = '午餐')
	dorm_choice = (('单人间','单人间'),('双人间','双人间'))
	need_dorm = models.CharField(max_length = 10,choices=dorm_choice,verbose_name = '酒店')
	area_choice = (('市区','市区'),('曹妃甸','曹妃甸'))
	area = models.CharField(max_length = 10,choices=area_choice,verbose_name = '地点')
	is_pay = models.BooleanField(verbose_name = '预报名支付',default=True)
	major_choice = (('医学','医学'),('建工','建工'),('其它','其它'),('管联','管联'))
	major = models.CharField(max_length = 10,choices=major_choice,verbose_name = '专业')
	class Meta:
		 verbose_name_plural='12月预报名'
	def __str__(self):	 	
		return self.name
class Student2(models.Model):
	name = models.CharField(max_length = 20,verbose_name='姓名',blank=False)
	qq = models.CharField(max_length = 12,blank=False)
	obj_school = models.CharField(max_length = 100,verbose_name = '报考学校',blank=False)
	obj_major = models.CharField(max_length = 100,verbose_name = '报考专业',blank=False)
	major = models.CharField(max_length = 100,blank=False,verbose_name = '所在专业')
	phone = models.CharField(max_length=11,blank=False,verbose_name = '手机号')

	is_return = models.CharField(max_length=40,blank=False,verbose_name = '单程/双程')
	is_need = models.BooleanField(blank=True,verbose_name = '12月份是否需要提供服务')
	is_enroll = models.CharField(max_length = 4,blank=False,verbose_name = '是否学员')
	sex = models.CharField(max_length=10,blank=False,verbose_name = '性别')
	modifed_date = models.DateTimeField(auto_now_add=True,verbose_name ='提交时间')
	ride_date = models.CharField(max_length=20,blank=False,verbose_name ='乘车日期')
	ride_time = models.CharField(max_length=20,blank=False,verbose_name ='乘车班次')
	price = models.CharField(max_length = 4,blank = False,verbose_name = '票价')
	class Meta:
		 verbose_name_plural='文都现场确认'
	def __str__(self):	 	
		return self.name
