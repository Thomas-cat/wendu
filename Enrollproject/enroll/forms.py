from django import forms
class StudentForm(forms.Form):
	name = forms.CharField(max_length = 20,strip=True,required=True)
	qq = forms.CharField(max_length = 12,min_length=6,strip=True,required=False)
	obj_school = forms.CharField(max_length = 100,strip=True,required=False)
	institute = forms.CharField(max_length = 100,strip=True,required=False)
	major = forms.CharField(max_length = 100,strip=True,required=False)
	phone = forms.CharField(max_length=11,min_length=11,strip=True,required=True)
	is_enroll = forms.BooleanField(required=False)
	fields = ['name','qq','obj_school','institute','major','phone','is_enroll']

