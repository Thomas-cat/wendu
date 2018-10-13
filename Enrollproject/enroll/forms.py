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


class StudentForm2(forms.Form):
	name = forms.CharField(max_length = 20,strip=True,required=True)
	qq = forms.CharField(max_length = 12,min_length=6,strip=True,required=True)
	obj_school = forms.CharField(max_length = 100,strip=True,required=True)
	obj_major = forms.CharField(max_length = 100,strip=True,required=True)

	sex = forms.ChoiceField(choices=(('男生','男生'),('女生','女生')),required=True)
	ride_date = forms.ChoiceField(choices=(('2018.11.07','2018.11.07'),('2018.11.08','2018.11.08'),('2018.11.09','2018.11.09')),required=True)
	ride_time = forms.ChoiceField(choices=(('06.30','06.30'),('07.00','07.00'),('12.00','12.00')),required=True)
	is_return = forms.ChoiceField(choices=((0,'------'),('单程','单程'),('回程','回程')),required=True,initial=0)
	major = forms.CharField(max_length = 100,strip=True,required=True)
	phone = forms.CharField(max_length=11,min_length=11,strip=True,required=True)
	is_enroll = forms.ChoiceField(choices=((0,'------'),('是','是'),('否','否')),required=False)

	is_need = forms.BooleanField(required=False)
	fields = ['name','qq','obj_school','major','phone','is_enroll','sex','is_need','is_return','ride_date','obj_major']
