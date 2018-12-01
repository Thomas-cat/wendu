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
	sex_choice = (('男生','男生'),('女生','女生'))
	sex = models.CharField(max_length = 4,choices=sex_choice,blank=True,verbose_name = '性别')
	phone = models.CharField(max_length=11,blank=False,verbose_name = '手机号')
	exam_choice = (
					('唐山市第十二中学(初中北院)','唐山市第十二中学(初中北院)'),
					('唐山市第二十六中学','唐山市第二十六中学'),
					('唐山市第三十中学(南校区)','唐山市第三十中学(南校区)'),
					('唐山市第五十二中学','唐山市第五十二中学'),
					('唐山市第五十四中学(主校区)','唐山市第五十四中学(主校区)'),
					('唐山市路北区七十号小学','唐山市路北区七十号小学'),
					('唐山市路北区龙泉西里小学','唐山市路北区龙泉西里小学'),
					('唐山市路北区扶轮小学','唐山市路北区扶轮小学'),
					('唐山市路北区鹭港小学','唐山市路北区鹭港小学'),
					('唐山市第一职业中','唐山市第一职业中'),
					('唐山市友谊中学(西校区)','唐山市友谊中学(西校区)'),
					('唐山市西山路小学','唐山市西山路小学'),
					('唐山师范学院附属小学','唐山师范学院附属小学'),
					)
	exam_area = models.CharField(max_length = 200,choices=exam_choice,verbose_name = '考点',blank=True)

	major_choice = (('医学','医学'),('建工','建工'),('其它','其它'),('管联','管联'))
	major = models.CharField(max_length = 10,choices=major_choice,verbose_name = '专业')

	area_choice = (('市区','市区'),('曹妃甸','曹妃甸'))
	area = models.CharField(max_length = 10,choices=area_choice,verbose_name = '地点')

	modifed_date = models.DateTimeField(auto_now_add=True,verbose_name ='提交时间')
	bus_choice = (('单程去','单程去'),('双程','双程'),('不需要','不需要'))
	need_bus = models.CharField(max_length = 10,choices=bus_choice,verbose_name = '大巴车')

	dorm_choice = (('单人间','单人间'),('双人间','双人间'))
	need_dorm = models.CharField(max_length = 10,choices=dorm_choice,verbose_name = '酒店')
	day_choice = (('1天','1天'),('2天','2天'))
	day_dorm = models.CharField(max_length = 4,choices=day_choice,blank=True,verbose_name = '住宿天数')
	lunch_choice = (('1天','1天'),('2天','2天'),('不需要','不需要'))
	need_lunch = models.CharField(max_length = 10,blank=True,choices=lunch_choice,verbose_name = '午餐')
	money = models.CharField(max_length = 4,blank=True,verbose_name = '金额')
	is_enroll = models.BooleanField(verbose_name = '已报名',default=False)
	is_pay = models.BooleanField(verbose_name = '预报名支付',default=True)
	all_pay = models.BooleanField(verbose_name = '正式报名支付',default=False)
	def save(self,*args,**kwargs):
		money = 0 
		if self.day_dorm == '1天':
			day1 = 1
		elif self.day_dorm == '2天':
			day1 = 2
		else:
			day1 = 0 
		if self.need_lunch == '1天':
			day2 = 1
		elif self.need_lunch == '2天':
			day2 = 2
		else:
			day2 = 0
		if self.need_bus == '单程去':
			money += 20	
		elif self.need_bus == '双程':
			money += 40	
		if self.need_dorm =='单人间':
			money +=day1*(200+40)
		elif self.need_dorm == '双人间':
			money +=day1*(100+40)
		money +=day2*15
		if money-100<0:
			self.money = 0
		else:
			self.money = money-100
		super(YuBaoMing,self).save(*args,**kwargs)
	class Meta:
		 verbose_name_plural='12月正式报名'
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
