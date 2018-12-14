from django import forms
import datetime

class StudentForm(forms.Form):
	name = forms.CharField(max_length = 20,strip=True,required=True)
	qq = forms.CharField(max_length = 12,min_length=6,strip=True,required=False)
	obj_school = forms.CharField(max_length = 100,strip=True,required=False)
	institute = forms.CharField(max_length = 100,strip=True,required=False)
	major = forms.CharField(max_length = 100,strip=True,required=False)
	phone = forms.CharField(max_length=11,min_length=11,strip=True,required=True)
	is_enroll = forms.BooleanField(required=False)
	fields = ['name','qq','obj_school','institute','major','phone','is_enroll']

class LoginForm(forms.Form):
	name = forms.CharField(max_length = 20,strip=True,required=True)
	phone = forms.CharField(max_length=11,min_length=11,strip=True,required=True)
	fields = ['name','phone']
class FormalEnrollForm(forms.Form):
	"""
	sex = forms.ChoiceField(choices=(('男生','男生'),('女生','女生')),required=True)
	area = forms.ChoiceField(choices=(('市区','市区'),('曹妃甸','曹妃甸')),required=True)
	"""
	exam = forms.ChoiceField(choices=(
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
					),required=True)
	fields = ["exam"]
class PreEnrollForm(forms.Form):
	name = forms.CharField(max_length = 20,strip=True,required=True)
	phone = forms.CharField(max_length=11,min_length=11,strip=True,required=True)
	major = forms.ChoiceField(choices=(('管联','管联'),('医学','医学(考试科目三科)'),('建工','建工(考试时间三天)'),('其它','其它')),required=True)
	area = forms.ChoiceField(choices=(('市区','市区'),('曹妃甸','曹妃甸')),required=True)
	need_bus = forms.ChoiceField(choices=(('单程去','单程去'),('双程','双程'),('不需要','不需要(市区)')),required=True,initial=0)
	need_dorm = forms.ChoiceField(choices=(('单人间','单人间'),('双人间','双人间')),required=True,initial=0)
	fields = ['name','phone','need_bus','need_dorm','area','major']

class StudentForm2(forms.Form):
	name = forms.CharField(max_length = 20,strip=True,required=True)
	qq = forms.CharField(max_length = 12,min_length=6,strip=True,required=True)
	obj_school = forms.CharField(max_length = 100,strip=True,required=True)
	obj_major = forms.CharField(max_length = 100,strip=True,required=True)

	sex = forms.ChoiceField(choices=(('男生','男生'),('女生','女生')),required=True)
	ride_date = forms.ChoiceField(choices=(('2018.11.07','2018.11.07'),('2018.11.08','2018.11.08'),('2018.11.09','2018.11.09')),required=True)
	ride_time = forms.ChoiceField(choices=(('06.30','06.30'),('07.00','07.00'),('12.00','12.00')),required=True)
	is_return = forms.ChoiceField(choices=(('单程','单程'),('双程','双程')),required=True,initial=0)
	is_enroll = forms.ChoiceField(choices=(('否','否'),('是','是')),required=True,initial=0)
	major = forms.CharField(max_length = 100,strip=True,required=True)
	phone = forms.CharField(max_length=11,min_length=11,strip=True,required=True)
	is_need = forms.BooleanField(required=False)
	fields = ['name','qq','obj_school','major','phone','sex','is_enroll','is_need','is_return','ride_date','obj_major']
